<!-- Packages -->

django

python-dotenv

djangorestframework

pytest

pytest django

black

flake8

django-mptt

drf-spectacular

coverage

pytest-cov

pytest-factoryboy

<!-- Commands -->

django-admin startproject ecommerce

py manage.py runserver

py manage.py shell --> from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())

exit()

pip install --upgrade pip

py manage.py spectacular --file schema.yml

coverage run -m pytest

coverage html

pytest --cov

<!-- Pytest -->

pytest -h <!-- prints options _and_ config file settings-->


<!-- To make VS Code recognize python code -->

1. Control+ shift + p.
2. type 'Python: Select Interpreter' and select the same.
3. choose your virtual env from the list if it is not listed please choose Enter Interpreter path'
4. Give pathe like this 'C:\Users\user\Desktop\Python\django-drf-ecommerce\env'


<!-- Useful links -->

https://www.django-rest-framework.org/api-guide/viewsets/
https://docs.djangoproject.com/en/4.2/ref/models/fields/