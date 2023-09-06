# Empower - Job Vacancies Management Project

Empower is a project developed for managing job vacancies and user orders. It provides features to create vacancies,
view job listings, manage user cards, and much more.

## Requirements

Before running the project, make sure you have the following dependencies installed:

- autopep8==2.0.2
- Python 3.x
- Django 4.2.3
- Django Rest Framework 3.14.0
- drf-yasg 1.21.6
- django_filters 23.2
- django-phonenumbers 1.0.1
- django-phonenumber-field 7.1.0
- openai 0.27.8
- Pillow 10.0.0
- psycopg2-binary 2.9.6
- PyJWT 2.7.0
- PyYAML 6.0
- python-dotenv 1.0.0
- requests 2.31.0
- typing_extensions 4.7.1
- Jinja2 3.1.2

## Installation

1. Clone the repository from GitHub:

   ```bash
   git clone https://github.com/arabiya5843/empower.git
   cd empower
   ```

   or

   ```bash
   git clone git@github.com:arabiya5843/empower.git
   cd empower
   ```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Set up the environment variables:

Create a `.env` file in the root directory and define the following environment variables:

```dotenv
DJANGO_SECRET_KEY=your_django_secret_key
DEBUG=True# Set to False in production
DATABASE_ENGINE=django.db.backends.postgresql_psycopg2
POSTGRES_DB=empower
POSTGRES_USER=your_postgres_username
POSTGRES_PASSWORD=your_postgres_password
DATABASE_HOST=your_database_host# Usually 'localhost' for local development
DATABASE_PORT=your_database_port# Default is 5432 for PostgreSQL
API_KEY=your_openai_api_key
```

4. Apply the database migrations:

```bash
python manage.py migrate
```

5. Create a superuser for administrative access:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

## Usage

After installation and starting the server, you can use the project for the following purposes:

- Create and view job vacancies
- Manage user cards
- Authenticate and authorize users using JWT tokens
- Filter vacancies based on various criteria

## Project Structure

The Empower project has the following structure:

```
empower/
├── apps/
│   ├── users/
│   ├── employment/
│   ├── orders/
│   shared/
├── root/
│   ├── .env
├── .gitignore
├── Makefile
├── manage.py
├── requirements.txt
```

The project is divided into several applications, each responsible for specific functionality, such
as `users`, `employment` and `orders`. More information about each application can be found in their
respective directories.

## Core Models and Functionality

[... Explanation about core models and functionality]

## API

The project provides APIs to work with job vacancies and user cards. The API documentation is available at `/swagger/`
after starting the server.

## Testing

The project includes tests for core functionalities. You can run the tests using the following command:

```bash
python manage.py test
```

## Makefile

The project includes a Makefile with several useful commands for development. Here are some common commands:

- `make mig`: Run database migrations.
- `make admin`: Create a superuser for the admin panel.
- `make unmig`: Delete database migrations except __init__.py.
- `make test`: Run tests.
- `make lint`: Run code linting checks.
- `make format`: Format code using autopep8.

Please make sure you have `make` installed on your system before using these commands.

## Deploying on Linux Ubuntu

To deploy the project on Linux Ubuntu, follow these steps:

1. Install required system packages:

```bash
sudo apt-get update
sudo apt-get install python3-dev python3-venv libpq-dev
```

2. Clone the repository and navigate to the project directory.

3. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install project dependencies:

```bash
pip install -r requirements.txt
```

5. Set up the `.env` file as described earlier with appropriate values for your production environment.

6. Collect static files:

```bash
python manage.py collectstatic
```

7. Run database migrations:

```bash
python manage.py migrate
```

8. Start the Gunicorn server:

```bash
gunicorn root.wsgi:application --bind 0.0.0.0:8000
```

9. Use a reverse proxy (e.g., Nginx) to handle incoming requests and serve the Gunicorn server.

Please note that this is a basic setup for deploying the project on Ubuntu. In a production environment, you should
consider additional configurations for security, scalability, and performance.

## Contributing

If you want to contribute to the project, you can fork the repository and submit your changes via a pull request.

## License

[Specify the license of your project, if any.]

## Authors
