Encrypt Pelican Content
===============

This plugin allows you to have password protected blog articles in [Pelican](http://docs.getpelican.com/). The 
articles are encrypted with AES-256 in Python using [PyCrypto](https://www.dlitz.net/software/pycrypto/), and 
decrypted in the browser with [Crypto-JS](https://code.google.com/p/crypto-js/). 

####Requirements

- Pelican 3.3+ (has not been tested on earlier versions)
- PyCrypto (`pip install pycrypto`)

####Installation

Copy the `encrypt_content` folder to the root of your Pelican project (or somewhere that is accessible for importing), and merge the `theme` folder with the theme folder for your Pelican project. 

Next, add the following to your `pelicanconf.py` file:

```python
PLUGINS = ['encrypt_content']
```

Now you need to modify three of your theme's template files in the `templates` directory. First, you need to make sure the article summary no longer shows up on the home page for encrypted articles. Find the following line in either `index.html`, or `post.html` (depending on your version of Pelican):

```jinja
{{ article.summary }}
```

Replace it with:

```jinja
{% include "encrypt_content/summary.html" with context %}
```

This will add the message "This content is encrypted." instead of the article summary. Go ahead and modify this message if you'd like.

Then, open up `article.html` and find the following line:

```jinja
{{ article.content }}
```

Replace it with:

```jinja
{% include "encrypt_content/content.html" with context %}
```

This will add in the encrypted content, and the form for entering the password.

Open `base.html` and add the following, just before the end of the `<body>` tag:

```jinja
{% include "encrypt_content/scripts.html" with context %}
```

This will add the script for decrypting the encrypted articles.

####Usage

Inside your article source file, just add the password of your choosing:

ex.

######reStructuredText

    How To Teach Your Horse To Make You Breakfast 
    ##############

    :date: 1983-04-22
    :tags: horses, food
    :password: presidentoftheuniverse


######Markdown

    Title: How To Teach Your Horse To Make You Breakfast
    Date: 1983-04-22
    Tags: horses, food
    Password: presidentoftheuniverse

####Other Uses

This will technically encrypt pages as well, if you want, but I never really saw the point. If you feel so inclined, you'll only need to modify `page.html` accordingly.

####Python 3 Support

I haven't tested this with Python 3, yet, but the python portion of the plugin is only about 40 LOC. If you happen to notice any problems with Python 3 and fix them, please submit a pull request.

####Also...

I'm not a crypto expert, so don't depend on this to hide plans for assassinating emperors or anything. 
