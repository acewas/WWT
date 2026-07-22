#!/usr/bin/env python
<<<<<<< HEAD
import os
import sys
=======
#.venv\Scripts\activate.ps1
import os
import sys
#docker run -d --name wwt-container -p 8000:8000 wwt-website:latest = RUNNING NEW CONTAINER
#docker start wwt-container = START A STOPPED CONTAINER

>>>>>>> developer


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Install dependencies with: pip install -r requirements.txt"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
