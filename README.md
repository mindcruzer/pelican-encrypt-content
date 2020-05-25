Encrypt Pelican Content
===============

This plugin allows you to have password protected articles and pages in [Pelican](http://docs.getpelican.com/). The 
content is encrypted with AES-256 in Python using [PyCryptodome](https://www.pycryptodome.org/), and 
decrypted in the browser with [Crypto-JS](https://code.google.com/p/crypto-js/).

#### Has been tested with

- Python 3.8
- Pelican 4.2.0
- PyCryptodome 3.9.7 (a PyCrypto fork)

Earlier versions of these might work, but no gaurantees.

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
