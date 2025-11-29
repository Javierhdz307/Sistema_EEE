from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()

try:
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="Admin12345"
        )
        print("Superusuario creado.")
    else:
        print("El superusuario ya existe.")
except IntegrityError:
    print("Error al crear el superusuario.")