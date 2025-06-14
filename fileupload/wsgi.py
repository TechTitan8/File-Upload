import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fileupload.settings')

# Vercel needs the variable to be named 'app'
application = get_wsgi_application()
app = application
