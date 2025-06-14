# Install system dependencies
apt-get update && apt-get install -y python3-dev

# Install Python dependencies
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput
