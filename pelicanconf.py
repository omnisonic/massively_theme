AUTHOR = 'jctech'
SITENAME = 'massively-theme'
SITEURL = ''

PATH = 'content'
THEME='html5up-massively_pelican_theme'
MENUITEMS = (('This is Massively','.'),)
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False


# Massivley variables:
FORMSPREE = 'https://formspree.io/f/xnqwdnle'
ADDRESS = ' set this variable in pelicanconf.py'
PHONE = ' set this variable in pelicanconf.py'
EMAIL = 'set this variable in pelicanconf.py'
TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ("github", "https://github.com/getpelican"),
    ("rss", "/blog/feeds/all.atom.xml"),
    ("twitter", "https://twitter.com/ThePSF")
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True