AUTHOR = 'Crola1702'
SITENAME = 'Cristobal Arroyo'
SITEURL = ""

PATH = "content"
ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARTICLE_URL = '{category}/{slug}.html'

TIMEZONE = 'America/Bogota'
DEFAULT_DATE_FORMAT = '%Y/%m/%d'

DEFAULT_LANG = 'es'

STATIC_PATHS = ['images', 'css']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("Full Stack Python", "https://www.fullstackpython.com/"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True