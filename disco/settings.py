"""
Django settings for disco project.
"""

import os
import arches
import inspect
import semantic_version
from django.utils.translation import gettext_lazy as _

from arches.settings import *

APP_NAME = 'disco'
APP_VERSION = semantic_version.Version(major=0, minor=0, patch=0)
APP_ROOT = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
MIN_ARCHES_VERSION = arches.__version__
MAX_ARCHES_VERSION = arches.__version__

WEBPACK_LOADER = {
    "DEFAULT": {
        "STATS_FILE": os.path.join(APP_ROOT, '..', 'webpack/webpack-stats.json'),
    },
}

DATATYPE_LOCATIONS.append('disco.datatypes')
FUNCTION_LOCATIONS.append('arches_for_science.pkg.extensions.functions')
FUNCTION_LOCATIONS.append('disco.functions')
ETL_MODULE_LOCATIONS.append('disco.etl_modules')
SEARCH_COMPONENT_LOCATIONS.append('disco.search_components')

LOCALE_PATHS.insert(0, os.path.join(APP_ROOT, 'locale'))
FILE_TYPE_CHECKING = False
FILE_TYPES = ["bmp", "gif", "jpg", "jpeg", "pdf", "png", "psd", "rtf", "tif", "tiff", "xlsx", "csv", "zip", "json"]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't*#3-h-$cj^1^c(g6f6%pn2&1-g@!5tk%k2!n0!ns(s@2ck!*1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ROOT_URLCONF = 'disco.urls'

# Modify this line as needed for your project to connect to elasticsearch with a password that you generate
ELASTICSEARCH_CONNECTION_OPTIONS = {"request_timeout": 30, "verify_certs": False, "basic_auth": ("elastic", "E1asticSearchforArche5")}

# If you need to connect to Elasticsearch via an API key instead of username/password, use the syntax below:
# ELASTICSEARCH_CONNECTION_OPTIONS = {"timeout": 30, "verify_certs": False, "api_key": "<ENCODED_API_KEY>"}
# ELASTICSEARCH_CONNECTION_OPTIONS = {"timeout": 30, "verify_certs": False, "api_key": ("<ID>", "<API_KEY>")}

# Your Elasticsearch instance needs to be configured with xpack.security.enabled=true to use API keys - update elasticsearch.yml or .env file and restart.

# Set the ELASTIC_PASSWORD environment variable in either the docker-compose.yml or .env file to the password you set for the elastic user,
# otherwise a random password will be generated.

# API keys can be generated via the Elasticsearch API: https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-create-api-key.html
# Or Kibana: https://www.elastic.co/guide/en/kibana/current/api-keys.html

# a prefix to append to all elasticsearch indexes, note: must be lower case
ELASTICSEARCH_PREFIX = 'disco'

ELASTICSEARCH_CUSTOM_INDEXES = []
# [{
#     'module': 'disco.search_indexes.sample_index.SampleIndex',
#     'name': 'my_new_custom_index', <-- follow ES index naming rules
#     'should_update_asynchronously': False  <-- denotes if asynchronously updating the index would affect custom functionality within the project.
# }]

KIBANA_URL = "http://localhost:5601/"
KIBANA_CONFIG_BASEPATH = "kibana"  # must match Kibana config.yml setting (server.basePath) but without the leading slash,
# also make sure to set server.rewriteBasePath: true

LOAD_DEFAULT_ONTOLOGY = False
LOAD_PACKAGE_ONTOLOGIES = True

# This is the namespace to use for export of data (for RDF/XML for example)
# It must point to the url where you host your site
# Make sure to use a trailing slash
ARCHES_NAMESPACE_FOR_DATA_EXPORT = "http://localhost:8000/"

# Webpack uses this address to request and compile template files
# It must point to the url where you host your site
# Make sure to use a trailing slash
PUBLIC_SERVER_ADDRESS = "http://localhost:8000/"

DATABASES = {
    "default": {
        "ATOMIC_REQUESTS": False,
        "AUTOCOMMIT": True,
        "CONN_MAX_AGE": 0,
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "HOST": "localhost",
        "NAME": "disco",
        "OPTIONS": {},
        "PASSWORD": "postgis",
        "PORT": "5432",
        "POSTGIS_TEMPLATE": "template_postgis",
        "TEST": {
            "CHARSET": None,
            "COLLATION": None,
            "MIRROR": None,
            "NAME": None
        },
        "TIME_ZONE": None,
        "USER": "postgres"
    }
}

INSTALLED_APPS = (
    "disco",
    "webpack_loader",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    "arches",
    "arches.app.models",
    "arches.management",
    "guardian",
    "captcha",
    "revproxy",
    "corsheaders",
    "oauth2_provider",
    "django_celery_results",
    "pgtrigger",
    # "silk",
    "arches_templating",
    "arches_for_science",
)

INSTALLED_APPS += ("arches.app",)

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    #'arches.app.utils.middleware.TokenMiddleware',
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "arches.app.utils.middleware.ModifyAuthorizationHeader",
    "oauth2_provider.middleware.OAuth2TokenMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    # "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "arches.app.utils.middleware.SetAnonymousUser",
    # "silk.middleware.SilkyMiddleware",
]

STATICFILES_DIRS = build_staticfiles_dirs(app_root=APP_ROOT)

TEMPLATES = build_templates_config(
    debug=DEBUG,
    app_root=APP_ROOT,
    context_processors=[
        "django.contrib.auth.context_processors.auth",
        "django.template.context_processors.debug",
        "django.template.context_processors.i18n",
        "django.template.context_processors.media",
        "django.template.context_processors.static",
        "django.template.context_processors.tz",
        "django.template.context_processors.request",
        "django.contrib.messages.context_processors.messages",
        "arches.app.utils.context_processors.livereload",
        "arches.app.utils.context_processors.map_info",
        "arches.app.utils.context_processors.app_settings",
        "arches_for_science.utils.context_processors.project_settings"
    ]
)

ALLOWED_HOSTS = []

SYSTEM_SETTINGS_LOCAL_PATH = os.path.join(APP_ROOT, 'system_settings', 'System_Settings.json')
WSGI_APPLICATION = 'disco.wsgi.application'

# URL that handles the media served from MEDIA_ROOT, used for managing stored files.
# It must end in a slash if set to a non-empty value.
MEDIA_URL = '/files/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT =  os.path.join(APP_ROOT)

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(APP_ROOT, "staticfiles")

# when hosting Arches under a sub path set this value to the sub path eg : "/{sub_path}/"
FORCE_SCRIPT_NAME = None

RESOURCE_IMPORT_LOG = os.path.join(APP_ROOT, 'logs', 'resource_import.log')
DEFAULT_RESOURCE_IMPORT_USER = {'username': 'admin', 'userid': 1}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'file': {
            'level': 'WARNING',  # DEBUG, INFO, WARNING, ERROR
            'class': 'logging.FileHandler',
            'filename': os.path.join(APP_ROOT, 'arches.log'),
            'formatter': 'console'
        },
        'console': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        }
    },
    'loggers': {
        'arches': {
            'handlers': ['file', 'console'],
            'level': 'WARNING',
            'propagate': True
        }
    }
}


# Sets default max upload size to 15MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 15728640

# Unique session cookie ensures that logins are treated separately for each app
SESSION_COOKIE_NAME = 'disco'

# For more info on configuring your cache: https://docs.djangoproject.com/en/2.2/topics/cache/
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
    'user_permission': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'user_permission_cache',
    },
}

# Hide nodes and cards in a report that have no data
HIDE_EMPTY_NODES_IN_REPORT = False

BYPASS_UNIQUE_CONSTRAINT_TILE_VALIDATION = False
BYPASS_REQUIRED_VALUE_TILE_VALIDATION = False

DATE_IMPORT_EXPORT_FORMAT = "%Y-%m-%d" # Custom date format for dates imported from and exported to csv

# This is used to indicate whether the data in the CSV and SHP exports should be
# ordered as seen in the resource cards or not.
EXPORT_DATA_FIELDS_IN_CARD_ORDER = False

#Identify the usernames and duration (seconds) for which you want to cache the time wheel
CACHE_BY_USER = {'anonymous': 3600 * 24}
TILE_CACHE_TIMEOUT = 600 #seconds
CLUSTER_DISTANCE_MAX = 5000 #meters
GRAPH_MODEL_CACHE_TIMEOUT = None

OAUTH_CLIENT_ID = ''  #'9JCibwrWQ4hwuGn5fu2u1oRZSs9V6gK8Vu8hpRC4'

APP_TITLE = 'Arches | Heritage Data Management'
COPYRIGHT_TEXT = 'All Rights Reserved.'
COPYRIGHT_YEAR = '2019'

ENABLE_CAPTCHA = False
# RECAPTCHA_PUBLIC_KEY = ''
# RECAPTCHA_PRIVATE_KEY = ''
# RECAPTCHA_USE_SSL = False
NOCAPTCHA = True
# RECAPTCHA_PROXY = 'http://127.0.0.1:8000'
if DEBUG is True:
    SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]


# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  #<-- Only need to uncomment this for testing without an actual email server
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = "xxxx@xxx.com"
# EMAIL_HOST_PASSWORD = 'xxxxxxx'
# EMAIL_PORT = 587

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

CELERY_BROKER_URL = "" # RabbitMQ --> "amqp://guest:guest@localhost",  Redis --> "redis://localhost:6379/0"
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = 'django-db' # Use 'django-cache' if you want to use your cache as your backend
CELERY_TASK_SERIALIZER = 'json'

CELERY_SEARCH_EXPORT_EXPIRES = 24 * 3600  # seconds
CELERY_SEARCH_EXPORT_CHECK = 3600  # seconds

CELERY_BEAT_SCHEDULE = {
    "delete-expired-search-export": {"task": "arches.app.tasks.delete_file", "schedule": CELERY_SEARCH_EXPORT_CHECK,},
    "notification": {"task": "arches.app.tasks.message", "schedule": CELERY_SEARCH_EXPORT_CHECK, "args": ("Celery Beat is Running",),},
}

# Set to True if you want to send celery tasks to the broker without being able to detect celery.
# This might be necessary if the worker pool is regulary fully active, with no idle workers, or if
# you need to run the celery task using solo pool (e.g. on Windows). You may need to provide another
# way of monitoring celery so you can detect the background task not being available.
CELERY_CHECK_ONLY_INSPECT_BROKER = False

CANTALOUPE_DIR = os.path.join(ROOT_DIR, "uploadedfiles")
CANTALOUPE_HTTP_ENDPOINT = "http://localhost:8182/"

ACCESSIBILITY_MODE = False
SEARCH_THUMBNAILS = True
# By setting RESTRICT_MEDIA_ACCESS to True, media file requests outside of Arches will checked against nodegroup permissions.
RESTRICT_MEDIA_ACCESS = False

# By setting RESTRICT_CELERY_EXPORT_FOR_ANONYMOUS_USER to True, if the user is attempting
# to export search results above the SEARCH_EXPORT_IMMEDIATE_DOWNLOAD_THRESHOLD
# value and is not signed in with a user account then the request will not be allowed.
RESTRICT_CELERY_EXPORT_FOR_ANONYMOUS_USER = False

# see https://docs.djangoproject.com/en/1.9/topics/i18n/translation/#how-django-discovers-language-preference
# to see how LocaleMiddleware tries to determine the user's language preference
# (make sure to check your accept headers as they will override the LANGUAGE_CODE setting!)
# also see get_language_from_request in django.utils.translation.trans_real.py
# to see how the language code is derived in the actual code

####### TO GENERATE .PO FILES DO THE FOLLOWING ########
# run the following commands
# language codes used in the command should be in the form (which is slightly different
# form the form used in the LANGUAGE_CODE and LANGUAGES settings below):
# --local={countrycode}_{REGIONCODE} <-- countrycode is lowercase, regioncode is uppercase, also notice the underscore instead of hyphen
# commands to run (to generate files for "British English, German, and Spanish"):
# django-admin.py makemessages --ignore=env/* --local=de --local=en --local=en_GB --local=es  --extension=htm,py
# django-admin.py compilemessages


# default language of the application
# language code needs to be all lower case with the form:
# {langcode}-{regioncode} eg: en, en-gb ....
# a list of language codes can be found here http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en"

# list of languages to display in the language switcher,
# if left empty or with a single entry then the switch won't be displayed
# language codes need to be all lower case with the form:
# {langcode}-{regioncode} eg: en, en-gb ....
# a list of language codes can be found here http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGES = [
#   ('de', _('German')),
    ('en', _('English')),
#   ('en-gb', _('British English')),
#   ('es', _('Spanish')),
]

# override this to permenantly display/hide the language switcher
SHOW_LANGUAGE_SWITCH = len(LANGUAGES) > 1

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

AWS_STORAGE_BUCKET_NAME = "disco-dev-test-bucket"

DOCKER=False

RENDERERS += [
    {
        "name": "fors-reader",
        "title": "ASD Hi Res FieldSpec4",
        "description": "Use for exports from all our ASD High Resolution Field Spectroscopy",
        "id": "88dccb59-14e3-4445-8f1b-07f0470b38bb",
        "iconclass": "fa fa-bar-chart-o",
        "component": "views/components/cards/file-renderers/fors-reader",
        "ext": "txt",
        "type": "text/plain",
        "exclude": "",
    },
    {
        "name": "xrf-reader",
        "title": "HP Spectrometer XRF ASCII Output",
        "description": "Use for exports from all our HP XRF outputs",
        "id": "31be40ae-dbe6-4f41-9c13-1964d7d17042",
        "iconclass": "fa fa-bar-chart-o",
        "component": "views/components/cards/file-renderers/xrf-reader",
        "ext": "txt",
        "type": "text/plain",
        "exclude": "",
    },
    {
        "name": "raman-reader",
        "title": "Raman File Reader",
        "description": "Use for exports from all our HP raman and gas chromatograph spectrometers",
        "id": "94fa1720-6773-4f99-b49b-4ea0926b3933",
        "iconclass": "fa fa-bolt",
        "component": "views/components/cards/file-renderers/raman-reader",
        "ext": "txt",
        "type": "text/plain",   
        "exclude": "",
    },
    {
        "name": "pdbreader",
        "title": "PDB File Reader",
        "description": "",
        "id": "3744d5ec-c3f1-45a1-ab79-a4a141ee4197",
        "iconclass": "fa fa-object-ungroup",
        "component": "views/components/cards/file-renderers/pdbreader",
        "ext": "pdb",
        "type": "",
        "exclude": "",
    },
    {
        "name": "pcdreader",
        "title": "Point Cloud Reader",
        "description": "",
        "id": "e96e84f2-bcb2-4ca4-8793-7568b09d7374",
        "iconclass": "fa fa-cloud",
        "component": "views/components/cards/file-renderers/pcdreader",
        "ext": "pcd",
        "type": "",
        "exclude": "",
    },
    {
        "name": "xy-reader",
        "title": "XY Data File Reader",
        "description": "Use for all instrument outputs with x-y data",
        "id": "e93b7b27-40d8-4141-996e-e59ff08742f3",
        "iconclass": "fa fa-bolt",
        "component": "views/components/cards/file-renderers/xy-reader",
        "ext": "txt",
        "type": "text/plain",   
        "exclude": "",
    },
]

X_FRAME_OPTIONS = "SAMEORIGIN"

FORMATS = [
    {"name": "Bruker M6 (point)", "id": "bm6", "renderer": "31be40ae-dbe6-4f41-9c13-1964d7d17042"},
    {"name": "Bruker 5g", "id": "b5g", "renderer": "31be40ae-dbe6-4f41-9c13-1964d7d17042"},
    {"name": "Bruker Tracer IV-V", "id": "bt45", "renderer": "31be40ae-dbe6-4f41-9c13-1964d7d17042"},
    {"name": "Bruker Tracer III", "id": "bt3", "renderer": "31be40ae-dbe6-4f41-9c13-1964d7d17042"},
    {"name": "Bruker 5i", "id": "b5i", "renderer": "31be40ae-dbe6-4f41-9c13-1964d7d17042"},
    {"name": "Bruker Artax", "id": "bart", "renderer": "31be40ae-dbe6-4f41-9c13-1964d7d17042"},
    {"name": "Renishaw InVia - 785", "id": "r785", "renderer": "94fa1720-6773-4f99-b49b-4ea0926b3933"},
    {"name": "Ranishsaw inVia - 633/514", "id": "r633", "renderer": "94fa1720-6773-4f99-b49b-4ea0926b3933"},
    {"name": "ASD FieldSpec IV hi res", "id": "asd", "renderer": "88dccb59-14e3-4445-8f1b-07f0470b38bb"},
]

XY_TEXT_FILE_FORMATS = ["dx", "txt"]

try:
    from .package_settings import *
except ImportError:
    try: 
        from package_settings import *
    except ImportError as e:
        pass

try:
    from .settings_local import *
except ImportError as e:
    try: 
        from settings_local import *
    except ImportError as e:
        pass

if DOCKER:
    try:
        from .settings_docker import *
    except ImportError: 
        try:
            from settings_docker import *
        except ImportError as e:
            pass

# returns an output that can be read by NODEJS

if __name__ == "__main__":
    transmit_webpack_django_config(**locals())