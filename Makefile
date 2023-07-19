mig:
	@echo "Running database migrations..."
	@python manage.py makemigrations
	@python manage.py migrate

admin:
	@echo "Creating superuser for the admin panel..."
	@./manage.py createsuperuser
	@echo "Superuser created."

unmig:
	@echo "Deleting database migrations except __init__.py..."
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	@echo "Database migrations deleted."
