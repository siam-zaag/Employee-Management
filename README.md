# Employee Management System

This is a Django-based web application designed to manage employs.

## Requirements

-   Python 3.x
-   Django 3.x or higher
-   Django REST framework
-   PostgreSQL (or any other preferred database)

## Setup Instructions

### Clone the Repository

```sh
git clone git@github.com:siam-zaag/employee_management.git
cd employee_management
```

### Create and Activate Virtual Environment

```sh
python -m venv task_venv
source task_venv/bin/activate  # On Windows use `task_venv\Scripts\activate`

```

### Install Dependencies

```sh
pip install -r requirements.txt
```

### Creating the requirements.txt File (if need- optional)

```sh
pip freeze > requirements.txt

```

### Run Migrations

```sh
python manage.py makemigrations
python manage.py migrate

```

### Create Superuser

```sh
python manage.py createsuperuser
```

### Run the Development Server

```sh
python manage.py runserver

```

### Access the Application

Open your web browser and go to http://127.0.0.1:8000/ to access the application.

### URL Endpoints

-   Home page: http://127.0.0.1:8000/
-   Add Employee: http://127.0.0.1:8000/add/
-   Edit Employee: http://127.0.0.1:8000/edit/2/

### URL Endpoints for admin portal

-   Edit Employee: http://127.0.0.1:8000/admin
