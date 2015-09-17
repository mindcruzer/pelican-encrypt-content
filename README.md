Encrypt Pelican Content
===============

This plugin allows you to have password protected articles and pages in [Pelican](http://docs.getpelican.com/). The 
content is encrypted with AES-256 in Python using [PyCrypto](https://www.dlitz.net/software/pycrypto/), and 
decrypted in the browser with [Crypto-JS](https://code.google.com/p/crypto-js/). 

This particular version will work with Python 3, but probably breaks competability with Python 2.

####Requirements

- Pelican 3.6+
- PyCrypto (`pip install pycrypto`)

####Installation

Copy the `encrypt_content` folder to the root of your Pelican project (or somewhere that is accessible for importing). 

Next, add the following to your `pelicanconf.py` file:

```python
PLUGINS = ['encrypt_content']
```

####Settings

You can set a summary, as well as a title prefix to use for all encrypted articles. The default for both is a 
blank string.

In  `pelicanconf.py` file:

```python
ENCRYPT_CONTENT = {
    'title_prefix': '[Encrypted]',
    'summary': 'This content is encrypted.'
}
```

####Usage

Inside your source file, just add the password of your choosing:

ex.

######reStructuredText

    That one time I robbed a bank 
    ###############################

    :date: 1983-04-22
    :tags: crime, banks, imabadass
    :password: correcthorsebatterystaple


######Markdown

    Title: That one time I robbed a bank
    Date: 1983-04-22
    Tags: crime, banks, imabadass
    Password: correcthorsebatterystaple


####Now with Python 3 Support

As an exercise in Python and git, I've maanged to get this awesome plugin by mindcruzer to work on Python 3.4.3. Most changes were dealing with Unicode encoding-decoding. I couldn't get the tuple of byte elements to decode within the structure, so I went for the ugly way and extracted each element.

####Earlier versions of Pelican

There is an older, crappier version of this plugin in the `pelican-3.3` branch. Go nuts.
