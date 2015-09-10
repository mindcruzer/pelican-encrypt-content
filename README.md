Encrypt Pelican Content
===============

This plugin allows you to have password protected articles and pages in [Pelican](http://docs.getpelican.com/). The 
content is encrypted with AES-256 in Python using [PyCrypto](https://www.dlitz.net/software/pycrypto/), and 
decrypted in the browser with [Crypto-JS](https://code.google.com/p/crypto-js/). 

####Requirements

- Pelican 3.6+ (has not been tested on earlier versions)
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
    ##############

    :date: 1983-04-22
    :tags: crime, banks, imabadass
    :password: correcthorsebatterystaple


######Markdown

    Title: That one time I robbed a bank
    Date: 1983-04-22
    Tags: crime, banks, imabadass
    Password: correcthorsebatterystaple


####Python 3 Support

I haven't tested this with Python 3 because I'm lazy, but the Python portion of the plugin is not long or complicated. If you happen to notice any problems with Python 3 and fix them, please submit a pull request.

####Earlier versions of Pelican

There is an older, crappier version of this plugin in the `pelican-3.3` branch. Go nuts.
