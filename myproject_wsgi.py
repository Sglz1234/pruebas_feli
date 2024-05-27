import os
import sys

# Añade el directorio de tu proyecto al path de Python
path = '/home/Sandraglez/pruebas_feli'
if path not in sys.path:
    sys.path.append(path)

# Ajusta el entorno para Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.py'

# Importa la aplicación Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


