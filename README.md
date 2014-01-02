Protect Content in Pelican
===============

This plugin allows you to have password protected blog articles in [Pelican](http://docs.getpelican.com/en/3.2/). The 
articles are encrypted with AES-256 in Python using [PyCrypto](https://www.dlitz.net/software/pycrypto/), and 
decrypted in the browser with [Crypto-JS](https://code.google.com/p/crypto-js/). 

####Installation

First,

    pip install pycrypto

Then, copy `/encrypt_content` to the root of your pelican folder (or somewhere that is accessible for importing). Next,
add the following to your `pelicanconf.py` file:

    PLUGINS = ['encrypt_content']

Then merge the `theme` folder, with the theme folder for your Pelican project.

Lastly, you need to modify `index.html`, `article.html`, and `base.html` accordingly. For `index.html`, we
don't want the summary to show up if the content is encrypted. Open up `theme/templates/index.html` in
your Pelican project and find the following line:

    {{ article.summary }}
    
and replace it with,

    {% include "encrypt-content-summary.html" with context %}

Then, open up `theme/templates/article.html` and find the following line:
include
    {{ article.content }}

and replace it with,

    {% include "encrypt-content-content.html" with context %}

Last, but most importantly, the scripts that do the actual decryption. I've included these scripts in the repo under
`theme/static/scripts/*`; you'll want to copy  to your theme folder. Next, you just need to include the script
in `theme/templates/base.html` of your Pelican project. Add the following, just before the end of the `<body>` tag:

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
