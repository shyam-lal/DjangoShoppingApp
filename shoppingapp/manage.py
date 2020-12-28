#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


#Apps folder
from os.path import abspath, dirname, join
from site import addsitedir
#Apps end


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shoppingapp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

"""
#APPs
sys.path.insert(0, join(settings.PROJECT_ROOT, "apps"))
#Apps
"""
#from django.conf import settings
#sys.path.append(os.path.join(settings.BASE_DIR, "apps"))


if __name__ == '__main__':
    main()