# restapi
REST APIs using Django.

Managing the user’s data using Django-REST-framework, a powerful and flexible toolkit for building Web APIs.

Requirements:

Python 3(recomandate 3.6.2 or above)
Django ( recomandate 2.0, or above)

Steps to be followed:

	Clone the central repo :
		https://github.com/kousikpanda2013/restapi.git

	Project setup:
		
		# Create a virtualenv to isolate our package dependencies locally
		virtualenv env
		source env/bin/activate  # On Windows use `env\Scripts\activate`

		# Install Django and Django REST framework into the virtualenv
		pip install django (ignore, if installed)
		pip install djangorestframework

	Now sync your database for the first time:

		python manage.py migrate			

	Testing our API:

		python manage.py runserver		

	Go to the browser, by going to the URL http://127.0.0.1:8000/api/user/?format=json