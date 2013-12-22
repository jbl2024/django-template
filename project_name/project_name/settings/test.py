from base import *

########## TEST SETTINGS
TEST_RUNNER = "ignoretests.DjangoIgnoreTestSuiteRunner"
IGNORE_TESTS = (
    # Apps to ignore. example : 'django.contrib.auth',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.'
)

########## IN-MEMORY TEST DATABASE
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}

########## SOUTH CONFIGURATION
SOUTH_TESTS_MIGRATE = False
########## END SOUTH CONFIGURATION
