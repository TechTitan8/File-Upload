# Django File Upload Project

## Setup Instructions

1. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create .env file in the project root with the following content (generate your own SECRET_KEY):
```bash
# Generate a secret key using:
# python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
SECRET_KEY=your-generated-secret-key
DEBUG=True
```

4. Run migrations:
```bash
python manage.py makemigrations files
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

7. Access the application:
- Admin interface: http://127.0.0.1:8000/admin/
- Login page: http://127.0.0.1:8000/login/
- Home page: http://127.0.0.1:8000/

## Features
- User authentication (login/logout)
- File upload (PDF, JPG, JPEG)
- File storage in SQLite database
- File download functionality
- Protected routes for authenticated users only
