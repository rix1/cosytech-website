"""
WSGI config for website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")

# Virtualenv
import site
import sys
PROJECT_ROOT = '/var/www/cosytech.net/cosytech-website/website/'
site_packages = os.path.join(PROJECT_ROOT, '../env/lib/python2.7/site-packages/')
site.addsitedir(os.path.abspath(site_packages))
sys.path.insert(0, site_packages)
sys.path.insert(0, PROJECT_ROOT)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


