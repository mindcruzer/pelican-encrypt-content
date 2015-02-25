"""
Copyright (c) 2015 Sean Stewart

Encrypt Content
-----------------
A pelican plugin to encrypt post content.
"""

import base64
import md5

from Crypto import Random
from Crypto.Cipher import AES

from pelican import signals


def encrypt(password, plaintext):
    """
    Produces the ciphertext bundle of plaintext content.

    Args:
        password: Password for decrypting the content
        plaintext: Byte string of post content

    Returns:
        Three-tuple of iv, ciphertext and padding character. iv and ciphertext
        are base64 encoded.
    """
    BLOCK_SIZE = 32
    PADDING_CHAR = '^'

    iv = Random.new().read(16)
    
    # key must be 32 bytes for AES-256
    key = md5.new()
    key.update(password)
    cipher = AES.new(key.digest(), AES.MODE_CBC, iv)

    # plaintext must be padded to be a multiple of BLOCK_SIZE
    plaintext_padded = plaintext + (BLOCK_SIZE - len(plaintext) % BLOCK_SIZE) * PADDING_CHAR
    ciphertext = cipher.encrypt(plaintext_padded)
    
    return (
        base64.b64encode(iv),
        base64.b64encode(ciphertext),
        PADDING_CHAR
    )


def protect_content(instance):
    """
    Called when the content object is initialized.
    """
    if 'password' in instance.metadata:
        # set new attributes for use in templates
        setattr(instance, 'protected', True)
        setattr(instance, 'encrypt', lambda content: "%s;%s;%s" % encrypt(
            instance.metadata['password'], 
            content.encode('utf8')
        ))


def register():
    signals.content_object_init.connect(protect_content)
