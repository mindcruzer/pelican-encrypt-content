Encrypt Pelican Content
===============

This plugin allows you to have password protected blog articles in [Pelican](http://docs.getpelican.com/). The 
articles are encrypted with AES-256 in Python using [PyCrypto](https://www.dlitz.net/software/pycrypto/), and 
decrypted in the browser with [Crypto-JS](https://code.google.com/p/crypto-js/). 

####Requirements

This plugin requires PyCrypto.

ex. 

```shell
pip install pycrypto
```

####Installation

Copy `encrypt_content` to the root of your Pelican project (or somewhere that is accessible for importing), and merge the `theme` folder with the theme folder for your Pelican project. Next,
add the following to your `pelicanconf.py` file:

```python
    PLUGINS = ['encrypt_content']
```

Lastly, you need to modify your theme template files `index.html`, `article.html`, and `base.html` accoringly. Open up `index.html` and find the following line:

```jinja
{{ article.summary }}
```

Replace it with:

```jinja
{% include "encrypt-content-summary.html" with context %}
```

Then, open up `article.html` and find the following line:

```jinja
{{ article.content }}
```

Replace it with:

```jinja
{% include "encrypt-content-content.html" with context %}
```

Open `base.html` and add the following, just before the end of the `<body>` tag:

```jinja
{% include "encrypt-content-scripts.html" with context %}
```

####Usage

Inside your article source file, just add the password of your choosing:

ex.

######reStructuredText

    How To Teach Your Horse To Make You Breakfast 
    ##############

    :date: 1983-04-22
    :tags: horses, food, omgnofuckingway
    :password: presidentoftheuniverse


######Markdown

    Title: How To Teach Your Horse To Make You Breakfast
    Date: 1983-04-22
    Tags: horses, food, omgnofuckingway
    Password: presidentoftheuniverse

####Other Uses

This will technically encrypt pages as well, if you want, but I never really saw the point. If you feel so inclined, 
you'll only need to modify `page.html` accordingly.

####Also...

I'm not a crypto expert, so don't depend on this to hide plans for assassinating emperors or anything. 
