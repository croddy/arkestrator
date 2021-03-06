from mdc3.settings import *

ADMINS = (
    ('Rev. Johnny Healey', 'rev.null@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mdc3_dev',                      # Or path to database file if using sqlite3.
        'USER': 'mdc3_dev',                      # Not used with sqlite3.
        'PASSWORD': 'g4mm4r4Y',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}

#CACHE_BACKEND = "memcached://127.0.0.1:11211/"
#CACHE_MIDDLEWARE_KEY_PREFIX="MDC3DEV"

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

PARSER_DIR='/var/mdc3_dev/parser'

HAYSTACK_SITECONF = 'mdc3.search_sites'
HAYSTACK_SEARCH_ENGINE = 'solr'
HAYSTACK_SOLR_URL = 'http://127.0.0.1:8080/solr-mdc3_dev'
