Encrypt Pelican Content
===============

This plugin allows you to have password protected blog articles in [Pelican](http://docs.getpelican.com/). The 
articles are encrypted with AES-256 in Python using [PyCrypto](https://www.dlitz.net/software/pycrypto/), and 
decrypted in the browser with [Crypto-JS](https://code.google.com/p/crypto-js/). 

####Requirements

This plugin requires PyCrypto.

    pip install pycrypto

####Installation

Copy `encrypt_content` to the root of your Pelican project (or somewhere that is accessible for importing), and merge the `theme` folder with the theme folder for your Pelican project. Next,
add the following to your `pelicanconf.py` file:

    PLUGINS = ['encrypt_content']

Lastly, you need to modify your theme template files `index.html`, `article.html`, and `base.html` accoringly. Open up `index.html` and find the following line:

    {{ article.summary }}
    
Replace it with:

    {% include "encrypt-content-summary.html" with context %}

Then, open up `article.html` and find the following line:

    {{ article.content }}

Replace it with:

    {% include "encrypt-content-content.html" with context %}

Open `base.html` and add the following, just before the end of the `<body>` tag:

    {% include "encrypt-content-scripts.html" with context %}

####Usage

This is the easy part. Inside your article source file, just add one more line of metadata:

    Title: ...
    Date: ...
    Tags: ...
    Password: onefinepassword

and carry on.

####Other Uses

This will technically encrypt pages as well, if you want, but I never really saw the point. If you feel so inclined, 
you'll only need to modify `page.html` accordingly.
