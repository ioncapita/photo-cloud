Django Project with Docker and PostgreSQL Setup
Prerequisites

Docker
Docker Compose
Git

Project Setup

DJANGO_ALLOWED_HOSTS=["*"]

# Build and Run the Project

Using Docker Compose

docker-compose build

# Run migrations

docker-compose run --rm app python manage.py makemigrations photo_cloud
docker-compose run --rm app python manage.py migrate photo_cloud

# Start the project

docker-compose up

The application will be available at http://localhost:8000

# Entering the Container

To access the container's bash shell:
exec -it django_container /bin/bash
