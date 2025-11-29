import os
import django

# 1) Cargar settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sistema_EEE.settings")
django.setup()

# 2) Ya podemos usar Django
from django.contrib.auth import get_user_model

User = get_user_model()

# 3) Mostrar los usuarios existentes (debug)
print("Usuarios en BD:", list(User.objects.values("id", "username")))

# 4) Crear superusuario si no existe
USERNAME = "admin"
PASSWORD = "Admin12345"   # temporal
EMAIL = "admin@example.com"

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(
        username=USERNAME,
        email=EMAIL,
        password=PASSWORD,
        is_active=True
    )
    print("Superusuario creado correctamente.")
else:
    print("El superusuario ya existe.")