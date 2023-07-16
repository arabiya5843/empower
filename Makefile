mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

admin:
	./manage.py createsuperuser

unmig:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete