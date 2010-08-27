# Django settings for hhdictionary project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Giedrius Kudelis', 'giedrius.kudelis@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'postgresql_psycopg2'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'giedrius'             # Or path to database file if using sqlite3.
DATABASE_USER = 'giedrius'             # Not used with sqlite3.
DATABASE_PASSWORD = 'kalambur4s'         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Vilnius'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/var/django/media/giedrius/hhdictionary/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://giedrius.kudelis.lt/django/giedrius/hhdictionary/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = 'http://giedrius.kudelis.lt/django/adminmedia/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '5g56egss9vq-4si8nm6_lsb0wfb$xl2%tn!%cue*r0=i0&-wc3'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'utils.context_processors.mediaUrl',
    'menu.context_processors.currentModule',
    'menu.context_processors.pathPrefix',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
	'/var/django/templates/giedrius',
	'/var/django/templates/giedrius/hhdictionary',
	'/var/django/giedrius/hhdictionary/menu/templates',
	'/var/django/giedrius/hhdictionary/dictionary/templates',
	'/var/django/giedrius/hhdictionary/news/templates',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.markup',
	'dictionary',
	'menu',
	'utils',
	'news',
    'tagging',
)

# config for currentModule context processor
PATH_PREFIX = '/django/giedrius/hhdictionary/'
DEFAULT_MODULE = 'dictionary'
