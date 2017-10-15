### Adding a Django App
https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/

Virtual Environments
python 3 comes with venv module that creates an isolated environment for installing packages
python3 -m venv <name-of-directory>

will create a virtual environment with python installed

from inside that folder run `$ . bin/activate`
to activate your virtual environment
you will see your folder name
now anything you install will be added to this virtual environment
if you run python, it runs python3


python has a framework called django used for server-side
where express is unopinionated do it yourself
django is batteries included. it includes an orm

pip is like npm
pip list will list the currently installed packages
pip list --format=columns to not have the annoying error
deactivate will deactivate the virtual environment
when in env it will install local to folder and not globally on your system wide environment


install django
`$ pip install django`
adds django-admin.py into bin
`$ django-admin.py startproject <directory-name>`
adds `db.sqlite3` `project-foler-name` `manage.py`
creates directory with manage.py inside and another dir with same name
`$ python manage.py runserver` to create a django dev server

dir with same name has files
```
__init__.py
settings.py
urls.py
wsgi.py
```



`python manage.py startapp <app-name>`
example `python manage.py startapp scrumtracker`
creates a new python package 'scrumtracker'
Basically generates a python module in its own directory
App has its own models, urls, views
A way for you to group your code into cleanly separated modules



open project in pycharm
must set correct project interpreter from pycharm settings > project > project interpreter
https://stackoverflow.com/questions/42145656/unresolved-reference-django-in-pycharm

### Django Model Classes
after setting data models
`python manage.py makemigrations`
what does this do? there is a migrationsfolder in our new app folder
makemigrations script generates a file into migrations folder
contains code that will allow us to use our models to enter data into the database
generates a schema

you can run this script with `python manage.py migrate`
```
outputs
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, scrumtracker, sessions
Running migrations:
  Applying scrumtracker.0001_initial... OK
```
this generates a file db.sqlite3, this is our database, good for dev, bad for prod

when adding something to models need to again run `python manage.py makemigrations`
```
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> None
```
because there is no data in our db currently, None will work

again need to `python manage.py migrate`

### Enabling the Admin Interface
now we will make changes to admin.py
```
from django.contrib import admin
from .models import List, Card

admin.site.register(List)
admin.site.register(Card)
```
and run `python manage.py createsuperuser`

checkout page again `python djangular/manage.py runserver`
go to http://127.0.0.1:8000/ and add admin to the end
http://127.0.0.1:8000/admin


### Installing django-rest-framework
`$ pip install djangorestframework`
```
Collecting djangorestframework
  Downloading djangorestframework-3.7.0-py2.py3-none-any.whl (1.5MB)
    100% |████████████████████████████████| 1.5MB 747kB/s
Installing collected packages: djangorestframework
Successfully installed djangorestframework-3.7.0
```
then in your app create a new
file called serializers.py
A serializer class is something that
translastes your model from python to JSON
We could write all of this by hand
but the rest_framework has a serializers
package and that contains
a class called model serializer
The model serializer will look
 at your Django model class,
look at all the fields and their types,
and automatically convert them into JSON.
Later on you can customize it and say
you want to leave out fields or add extra stuff,
but for now this is all we need.
I import both of my model classes,
and for each I make a serializer.

I have a list serializer that inherits from
serializer.ModelSerializer.
Then I have to tell it that the model class
it has to convert to JSON is my list model.
I do that by adding another class inside
the serializer class called Meta.
Inside that class, I say the model
I'm representing is list.
For card serializer, it's exactly the same.
We inherit from serializers.ModelSerializer
add an inner class Meta, and say model is a card.
And that's all. These classes will look
at our cards and lists and be able
to translate them to JSON.
So suppose, in my scrumtracker app
a user comes in and wants to see all
of his cards. We already have a way to
store cards and to convert them to JSON,
now I need a way to actually serve those
to the angular front end.
For that, I have another new file called API.
```

have to add fields = '__all__' in serializesrs
```
from rest_framework import serializers

from .models import List, Card

class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'


class ListSerializer(serializers.ModelSerializer):
    cards = CardSerializer(read_only=True, many=True)
    class Meta:
        model = List
        fields = '__all__'
```
