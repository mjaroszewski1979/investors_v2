#!/bin/sh

# Apply any pending database schema changes based on model changes
python manage.py makemigrations 

# Apply those changes to the database
python manage.py migrate 

# Create a superuser for the Django admin interface
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell 

# Start the Django development server on all available network interfaces, port 8000
python manage.py runserver 0.0.0.0:8000


