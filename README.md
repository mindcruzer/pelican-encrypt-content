Protect Content in Pelican
===============

This plugin allows you to have password protected blog articles in [Pelican](http://docs.getpelican.com/en/3.2/). The 
articles are encrypted with AES-256 in Python using [PyCrypto](https://www.dlitz.net/software/pycrypto/), and 
decrypted in the browser with [Crypto-JS](https://code.google.com/p/crypto-js/). 

####Installation

First,

    pip install pycrypto

Then, copy `/protect_content` to the root of your pelican folder (or somewhere that is accessible for importing). Next, 
add the following to your Pelican settings file:

    PLUGINS = ['protect_content']
    
That takes care of encrypting the content. When content is encrypted, two properties are added to the `Content` 
instance: `protected`, which is a flag that states whether or not the content is encrypted, and `encrypted_content` 
which contains the ciphertext bundle (iv, ciphertext, padding character).

The last thing on the agenda is to modify `index.html`, `article.html`, and `base.html` accordingly. For `index.html`, you basically 
want to make sure that the article summary doesn't show up for protected content. Open up `theme/templates/index.html` in
your Pelican project and find the following line:

    {{ article.summary }}
    
and replace it with,

    {% if article.protected %}
    <i>This content is encrypted.</i>
    {% else %}
    {{ article.summary }}
    {% endif %}

Then, open up `theme/templates/article.html` and find the following line:

    {{ article.content }}

and replace it with,

    {% if article.protected %}
    <div id="encrypted-content" style="display:none">{{ article.encrypted_content }}</div>
    <div id="decrypted-content">
        <h4><i>This content is encrypted.</i></h4>
    </div>
    <form id="unlock-form">
        <label for="content-password">Password</label>
        <input type="password" id="content-password" placeholder="Password" />
        <button type="button" id="unlock-content">Unlock</button>
    </form>
    {% else %}
    {{ article.content }}
    {% endif %}

This should be straightforward. If the content is protected, output the ciphertext bundle instead of the 
plaintext, then add a form for entering the password. 

Last, but most importantly, the scripts that do the actual decryption. I've included these scripts in the repo under 
`theme/static/scripts/*`; you'll want to copy these to your theme folder. Next, you just need to include the scripts 
in `theme/templates/base.html` of your Pelican project. Add them just before the end of the `<body>` tag, in the 
following order:

    <script type="text/javascript" src="{{ SITEURL }}/theme/scripts/md5.js"></script>
    <script type="text/javascript" src="{{ SITEURL }}/theme/scripts/aes.js"></script>
    <script type="text/javascript" src="{{ SITEURL }}/theme/scripts/pad-nopadding-min.js"></script>
    <script type="text/javascript" src="{{ SITEURL }}/theme/scripts/protect_content.js"></script>
    
That or concat, minify and only add one file. If you can be bothered, it would be better if you
threw these in their own template, say `protected_content.html` and then included it in `base.html` with 
`{% include 'protected_content.html %}`, just to keep things tidy.

####Usage

This is the easy part. Inside your article source file, just add one more line of metadata:

    Title: ...
    Date: ...
    Tags: ...
    Password: iamthepassword
    
BOOM! Encrypted articles.

####Other Uses

This will technically encrypt pages as well, if you want, but I never really saw the point. If you feel so inclined, 
you'll only need to modify `page.html` accordingly.
