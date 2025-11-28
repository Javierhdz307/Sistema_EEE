import os
import sys

# Ruta absoluta hacia manage.py (AJÚSTALA si es necesario)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
manage_path = os.path.join(BASE_DIR, 'manage.py')

# Comando para iniciar Django
os.system(f'"{sys.executable}" "{manage_path}" runserver 0.0.0.0:8000')