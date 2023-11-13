# Setup script allowing notebooks to behave like a Django shell
import sys, os, django

from pathlib import Path


# Find the project base directory (containing all app folders)
BASE_DIR = Path(__file__).resolve().parent.parent

# Add the base directory to sys.path. This allows importing from apps like when
# running a Django shell
sys.path.insert(0, str(BASE_DIR))

# Access Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_jupyter.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"  # ORM is sync-only

# Initialize Django
django.setup()
