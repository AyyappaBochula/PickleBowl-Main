import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backend.settings')
django.setup()

from django.contrib.auth import get_user_model
from adminpanel.models import AdminUser

User = get_user_model()

# 1. Create Django Superuser (for /superadmin/)
SUPERUSER_USERNAME = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
SUPERUSER_EMAIL = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@picklebowl.com')
SUPERUSER_PASSWORD = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'Admin@123456')

if not User.objects.filter(username=SUPERUSER_USERNAME).exists():
    User.objects.create_superuser(
        username=SUPERUSER_USERNAME,
        email=SUPERUSER_EMAIL,
        password=SUPERUSER_PASSWORD
    )
    print(f"[OK] Superuser '{SUPERUSER_USERNAME}' created successfully.")
else:
    print(f"[INFO] Superuser '{SUPERUSER_USERNAME}' already exists.")

# 2. Create Custom Store Admin User (for /admin/)
ADMIN_MOBILE = os.environ.get('ADMIN_MOBILE', '9876543210')
ADMIN_NAME = os.environ.get('ADMIN_NAME', 'PickleBowl Admin')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'Admin@123456')

if not AdminUser.objects.filter(mobile=ADMIN_MOBILE).exists():
    AdminUser.objects.create(
        name=ADMIN_NAME,
        mobile=ADMIN_MOBILE,
        password=ADMIN_PASSWORD,
        role='superadmin',
        is_active=True
    )
    print(f"[OK] Custom Store Admin '{ADMIN_MOBILE}' created successfully.")
else:
    print(f"[INFO] Custom Store Admin '{ADMIN_MOBILE}' already exists.")
