#!/usr/bin/env python3
"""Django's command-line utility for administrative tasks."""
import os
import sys
import os
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    execute_from_command_line(["manage.py", "runserver", "0.0.0.0:{}".format(port)])

# if 'DJANGO_SETTINGS_MODULE' not in os.environ:
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SILproject.settings')


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SILproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Set DEBUG to True for local development
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
