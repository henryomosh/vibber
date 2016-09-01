import os
    import sys

    sys.path.append('CC:/Users/omosh/Desktop/DJANGO PROJETS/djangoProject2')
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

    import django.core.handlers.wsgi
    application = django.core.handlers.wsgi.WSGIHandler()