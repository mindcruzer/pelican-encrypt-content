Encrypt Pelican Content
===============

This plugin allows you to have password protected articles and pages in [Pelican](http://docs.getpelican.com/). The 
content is encrypted with AES-256 in Python using [PyCryptodome](https://www.pycryptodome.org/), and 
decrypted in the browser with [Crypto-JS](https://code.google.com/p/crypto-js/). It has been tested in Python 3.8.0

#### Python 3.8 compatibility

PyCrypto is not compatible with Python 3.8 (https://github.com/dlitz/pycrypto/issues/283) and wasn't updated since 2014.
It has been widely and pretty smoothly replaced by [PyCryptodome](https://github.com/Legrandin/pycryptodome), 
a PyCrypto fork.

#### Requirements

- Pelican 4.2.0
- PyCryptodome 3.9.7
- Twisted 20.3.0 for tests

#### Installation

Copy the `encrypt_content` folder to the root of your Pelican project (or somewhere that is accessible for importing). 

Next, add the following to your `pelicanconf.py` file:

```python
PLUGINS = ['encrypt_content']
```

#### Settings

You can set a summary, as well as a title prefix to use for all encrypted articles. The default for both is a 
blank string.

In  `pelicanconf.py` file:

```python
ENCRYPT_CONTENT = {
    'title_prefix': '[Encrypted]',
    'summary': 'This content is encrypted.'
}
```

#### Usage

Inside your source file, just add the password of your choosing:

ex.

###### reStructuredText

    That one time I robbed a bank 
    ###############################

    :date: 1983-04-22
    :tags: crime, banks, imabadass
    :password: correcthorsebatterystaple


###### Markdown

    Title: That one time I robbed a bank
    Date: 1983-04-22
    Tags: crime, banks, imabadass
    Password: correcthorsebatterystaple
