# Django settings for giftReg project.


import os.path


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Alex McCool', 'alex.mccool@yahoo.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'postgresql_psycopg2'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'giftreg'             # Or path to database file if using sqlite3.
DATABASE_USER = 'giftreg'             # Not used with sqlite3.
DATABASE_PASSWORD = 'giftreg'         # Not used with sqlite3.
DATABASE_HOST = 'cindy'             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static'

STATIC_DOC_ROOT = os.path.join(os.path.dirname(__file__), 'static').replace('\\','/')
#MEDIA_DOC_ROOT = os.path.join(os.path.dirname(__file__), 'media').replace('\\','/')


# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

#ADMIN_TOOLS_MEDIA_URL = '/media/'


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'iweg(8e8+$tf*g6%02lz5*r@8ws6$oz9#^-ljnuw!#*iaq^rlu'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    # default template context processors
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',

    # django 1.2 only
    'django.contrib.messages.context_processors.messages',

    # required by django-admin-tools
    'django.core.context_processors.request',
)




MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)

#ROOT_URLCONF = 'giftreg.urls'
ROOT_URLCONF = 'urls'


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #'/home/amccool/giftreg/djangoGiftReg/giftReg/templates',
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
)

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    
    'giftreg',
    'debug_toolbar', 
    'django_extensions',
    'registration',
    'dajaxice',
    'profiles',
    'currencies',
)


ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.

LOGIN_REDIRECT_URL = '/'

#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = '@gmail.com'
#EMAIL_HOST_PASSWORD =''
#EMAIL_PORT = 587




INTERNAL_IPS = (
                '127.0.0.1',
                '192.168.2.50',
                '192.168.2.112',
                )


DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
#    'debug_toolbar.panels.timer.TimerDebugPanel',
#    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
#    'debug_toolbar.panels.headers.HeaderDebugPanel',
#    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
#    'debug_toolbar.panels.sql.SQLDebugPanel',
#    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

def custom_show_toolbar(request):
    return True # Always show toolbar, for example purposes only.

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
    #'EXTRA_SIGNALS': ['myproject.signals.MySignal'],
    'HIDE_DJANGO_SQL': False,
    'TAG': 'div',
}




DAJAXICE_FUNCTIONS = (
                      'giftreg.ajax.helloworld',
                      'giftreg.ajax.dajaxice_example',
                      )

DAJAXICE_MEDIA_PREFIX="dajaxice" # Will create http://yourdomain.com/dajaxice/.


ACCOUNT_ACTIVATION_DAYS=7
EMAIL_HOST='cindy'
DEFAULT_FROM_EMAIL = 'giftregistry@giftregistry.org'
LOGIN_REDIRECT_URL = '/giftReg'
#EMAIL_PORT=1023
#EMAIL_HOST_USER='username'
#EMAIL_HOST_PASSWORD='password'

AUTH_PROFILE_MODULE = "giftreg.UserProfile"




