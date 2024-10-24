import os
import django

from django.conf import settings
from django.template.utils import get_app_template_dirs


# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sudoku_forum.settings')

# Setup Django
django.setup()

print("Template directories:")
for template_dir in settings.TEMPLATES[0]['DIRS']:
    print(template_dir)

# Get app template directories
app_template_dirs = get_app_template_dirs('templates')
for dir in app_template_dirs:
    print(dir)
