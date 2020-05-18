"""
Copyright (c) 2015 Sean Stewart

Encrypt Content
-----------------
A pelican plugin to password protect content.

"""
import os
import base64
import hashlib

from Crypto import Random
from Crypto.Cipher import AES
from jinja2 import Template

from pelican import signals, generators
from pelican.utils import pelican_open

JS_LIBRARIES = [
    '//cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.2/components/core.js',
    '//cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.2/components/enc-base64.js',
    '//cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.2/components/cipher-core.js',
    '//cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.2/components/pad-nopadding.js',
    '//cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.2/components/md5.js',
    '//cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.2/components/aes.js'
]

PLUGIN_DIR = os.path.dirname(os.path.realpath(__file__))
DECRYPT_FORM_TPL_PATH = os.path.join(PLUGIN_DIR, 'decrypt-form.tpl.html')

with pelican_open(DECRYPT_FORM_TPL_PATH) as template:
    DECRYPT_FORM_TPL = template

settings = {
    'title_prefix': '',
    'summary': ''
}


def hash_md5(text):
    """
    Creates an md5 hash from text. 
    """
    key = hashlib.md5()
    key.update(text.encode('utf-8'))
    return key


def encrypt_text_aes(text, password):
    """
    Encrypts text with AES-256. 
    """
    BLOCK_SIZE = 32
    PADDING_CHAR = b'^'

    iv = Random.new().read(16)
    
    # key must be 32 bytes for AES-256, so the password is hashed with md5 first
    cipher = AES.new(hash_md5(password).digest(), AES.MODE_CBC, iv)

    plaintext = text.encode('utf-8')
    
    # plaintext must be padded to be a multiple of BLOCK_SIZE
    plaintext_padded = plaintext + (BLOCK_SIZE - len(plaintext) % BLOCK_SIZE) * PADDING_CHAR
    ciphertext = cipher.encrypt(plaintext_padded)
    
    return (
        base64.b64encode(iv),
        base64.b64encode(ciphertext),
        PADDING_CHAR
    )


def encrypt_content(content):
    """
    Replaces page or article content with decrypt form.
    """
    ciphertext_bundle = encrypt_text_aes(content._content, content.password)

    decrypt_form = Template(DECRYPT_FORM_TPL).render({
        'summary': settings['summary'],
        # this benign decoding is necessary before writing to the template, 
        # otherwise the output string will be wrapped with b''
        'ciphertext_bundle': b';'.join(ciphertext_bundle).decode('ascii'),
        'js_libraries': JS_LIBRARIES
    })

    content._content = decrypt_form
    content.title = '%s %s' % (settings['title_prefix'], content.title)
    content._summary = settings['summary']


def pelican_initialized(pelican_obj):
    """
    Reads settings.
    """
    try:
        settings.update(pelican_obj.settings['ENCRYPT_CONTENT'])
    except KeyError:
        pass


def pelican_all_generators_finalized(content_generators):
    """
    Finds pages and articles/article.drafts marked with a password and processes them.
    """
    for generator in content_generators:
        if isinstance(generator, generators.ArticlesGenerator):
            for article in generator.articles + generator.translations:
                if hasattr(article, 'password'):
                    encrypt_content(article)
            for draft in generator.drafts + generator.drafts_translations:
                if hasattr(draft, 'password'):
                    encrypt_content(draft)
        if isinstance(generator, generators.PagesGenerator):
            for page in generator.pages:
                if 'password' in page.metadata:
                    encrypt_content(page)


def register():
    signals.initialized.connect(pelican_initialized)
    signals.all_generators_finalized.connect(pelican_all_generators_finalized)
