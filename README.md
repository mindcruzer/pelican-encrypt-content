Encrypt Pelican Content
===============

This plugin allows you to have password protected articles and pages in [Pelican](http://docs.getpelican.com/). The 
content is encrypted with AES-256 in Python using [PyCryptodome](https://www.pycryptodome.org/), and 
decrypted in the browser with [Crypto-JS](https://code.google.com/p/crypto-js/).

### Installation

Refer to [How to use plugins](https://docs.getpelican.com/en/latest/plugins.html#how-to-use-plugins) in the Pelican docs.

#### Quick summary
Pelican 4.5 switched to namespace packages for plugins. Run `python setup.py install` and Pelican will auto-detect the plugin. 

Verify installation by running `pelican-plugins`. You should see something like:

```
-> Plugins found:
  | pelican.plugins.encrypt_content
```

#### Alternative method

Copy the `pelican/plugins` folder from this repository into the top level of your pelican project, then add the 
following to `pelicanconf.py`:

```
PLUGIN_PATHS = ['plugins']
PLUGINS = ['encrypt_content']
```

### Settings

You can set a summary, as well as a title prefix to use for all encrypted articles. The default for both is a 
blank string.

In  `pelicanconf.py` file:

```python
ENCRYPT_CONTENT = {
    'title_prefix': '[Encrypted]',
    'summary': 'This content is encrypted.'
}
```

### Usage

Inside your source file, just add the password of your choosing:

ex.

##### reStructuredText

    That one time I robbed a bank 
    ###############################

    :date: 1983-04-22
    :tags: crime, banks, imabadass
    :password: correcthorsebatterystaple


##### Markdown

    Title: That one time I robbed a bank
    Date: 1983-04-22
    Tags: crime, banks, imabadass
    Password: correcthorsebatterystaple
