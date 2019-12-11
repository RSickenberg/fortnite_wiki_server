"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from app.config import import_env_vars, get_project_root_path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
import_env_vars(os.path.join(get_project_root_path(), 'envdir'))

application = get_wsgi_application()
