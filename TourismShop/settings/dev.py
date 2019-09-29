from TourismShop.settings.settings import *  # NOQA (ignore all errors on this line)

import os


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite'),  # NOQA (ignore all errors on this line)
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.environ.get('DATABASE_NAME'),
        'NAME': 'tourismweb',
        'USER': 'charolim',
        'PASSWORD': '123'
    }
}