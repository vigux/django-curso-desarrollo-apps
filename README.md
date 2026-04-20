# Curso para desarrollar una aplicación web con el framework django

## Revisar versión de Python
Python --version

## Crear entorno virtual
 python -m venv .venv

## Activamos el entorno virtual
.venv\Scripts\activate

## Upgrade pip 
python -m pip install --upgrade pip

## Instalar el cliente de MySQL
pip uninstall mysqlclient -y; pip install --only-binary :all: mysqlclient

## instalar requirements
 pip install -r requierements.txt

## Realizar migraciones
python manage.py migrate

## Crear Super usuario para el panel Administrador y establecer una contraseña
python manage.py createsuperuser

## Habilitar Hosts
ALLOWED_HOSTS = ['*']

## Agregar Middleware whitenose  
'whitenoise.middleware.WhiteNoiseMiddleware',  # Add Whitenoise for static files

## Configurar rutas estaticas 
'DIRS': [BASE_DIR / 'templates'],

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

## Recopilar estaticos
python manage.py collectstatic --noinput

## Ejecutar servidor web
cd mi_proyecto
waitress-serve --port=8000 mi_proyecto.wsgi:application

## Comando para verificar direccion ip local
ipconfig

Desde el navegador accedemos con la direccion ip de la red local y probamos que todo funcione correctamente

## Comando para generar archivo de requerimientos:
pip freeze > requirements.txt