# Django CRM Project

This is a simple **Django-based CRM** with essential features like login, logout, Google authentication, password reset, and student record management. The application allows viewing, editing, and deleting individual student records.

## Features

- **Login and Logout**: Users can log in and log out of the CRM.
- **Google Authentication**: Users can log in using their Google account.
- **Forget Password**: Users can reset their passwords using the forget password functionality.
- **Student Records Management**: 
  - View individual student records.
  - Edit student records.
  - Delete student records.
- **Docker Support**: The project is containerized using Docker for easy deployment.

## Requirements

Before running the project, make sure you have the following installed:

- **Python 3.x**
- **Docker** (optional for Docker setup)
- **Docker Compose** (if using Docker)

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject



Create a virtual environment to isolate the project dependencies:

python -m venv venv


On Windows:

.venv\Scripts\activate

Install the required dependencies:

pip install -r requirements.txt



If the requirements.txt file doesn't exist, you can generate it by running:

pip freeze > requirements.txt


Run database migrations to set up the database schema:

python manage.py migrate


To access the Django admin panel and manage records, create a superuser:

python manage.py createsuperuser


You can run the project locally using Django’s development server:


python manage.py runserver


Build the Docker image:

docker-compose build


Start the Docker container:


docker-compose up
