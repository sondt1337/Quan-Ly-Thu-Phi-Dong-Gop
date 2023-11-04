#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD:myproject/manage.py
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quanlythuphidonggop.settings')
>>>>>>> 3f016ca0bc73209508bc0e8457c8a967bc5544c5:manage.py
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
