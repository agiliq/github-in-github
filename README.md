Takes a github account, creates html pages for it, 
and puts it on github pages.

How it proceeds.

1. Get data for specified account from Github API
2. Uses Jinja2 to write ReST docs.
3. Build html from the ReST docs.
4. Pushes the html to a Git repo from which you build github pages.

tl;dr: Yo dawg, I heard you like github, so I put a github in your github,
so you can github while you github.

Installation
--------------------------

1. Git clone
2. Create sercrets.py from secrets.example.py
3. edit settings.py
4. (optional) Edit build/conf_override.py to edit sphinx settings.
5. ./github_in_github.py
6. Here be magic.

Example
-----------------

Example page generated.

* [agiliq.github.com](http://agiliq.github.com)
* [shabda.github.com](http://shabda.github.com)

If you generate a page with this tell me, and will list it here.

Bug Reports
--------------
Open a ticket at github or email shada@agiliq.com


