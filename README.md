# E-Hood
A web application that allows you to be in the loop about everything happening in your neighborhood.

## Author and contact details
* MungaiKeren
Email: wambukeren@gmail.com

# Project Description
A user of the application should be able to:

1. Sign in with the application to start using.
2. Set up a profile about me and a general location and my neighborhood name.
3. Find a list of different businesses in my neighborhood.
4. Find Contact Information for the health department and Police authorities near my neighborhood.
5. Create Posts that will be visible to everyone in my neighborhood.
6. Change My neighborhood when I decide to move out.
7. Only view details of a single neighborhood.
A search functionality is implemented where one can search for the different businesses and their images.

# SetUp and installation requirements
You need to have the following installed:
* Python3+
* Pip ```curl https://bootstrap.pypa.io/get-pip|python```
* Virtual ```$ python3.6 -m venv pip virtual```
* Activate the virtual environment ```source virtual/bin/activate```
* Django==2.2.6 ```(virtual)$ pip install django==2.2.6```
* Get all requirements ```pip freeze > requirements.txt```

### Setting up the database
The database in use for this project is Postgres
* Ensure postgress is installed. ``` $ sudo apt-get update```
* Step 2 ```sudo apt-get install postgresql postgresql-contrib```

## Connect to postregsql
* ``` $ sudo su - postgres```
* ``` $ psql ```

## Set up the database to the django application
In the settings.py file,

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hoody',
        'USER': '< your postgres user name>',
        'PASSWORD': '< the database password>'
    }
}

### Run migrations
``` $ python manage.py makemigrations ```
``` $ python manage.py migrate ```


### Running the server
```python manage.py runserver```

# Behaviour Driven Development
Some of the behaviours in this application include;

| Input        | Output           | Behavior  |
| ------------- |:-------------:| -----:|
| Launch the site | User has to login or sign up before using the application | User is updated |
| Login | User is directed to create profile page | user is logged in |
| Create profile | Profile is updated and hood updated | users details are stored. |
| User can only view their hood details | User can change hood detaols in the app | Hood details are displayed|
| Add business | User can add business in different neighbourhoods | Business is added and displayed on homepage|
| Post a notice | Notice displayed can only be viewed by the users of that neighbourhood | neighbours are updated in the neighbourhood|

## Technologies used
* Django a python frame-work
* Javascript
* Html
* Bootstrap

# Development
It would be so great to have your contributions! Just follow the instructions below.

Fork the repo
* Clone the repo in your machine but ensure you have all the necessary modules.(You can find them in the set up instructions above) git clone https://github.com/MungaiKeren/Me-gallery.git
* Create a new branch git branch contributions
* Edit your changes in your branch
* Run the application
* Push your changes so we can have a view!

# Live development
Currently the app is deployed to heroku. You can find it [here](https://neibourhood.herokuapp.com/)

## Known Bugs
Currently there are no known bugs in this application


## Visual Representation
<img src="https://github.com/MungaiKeren/My-Shoe-images/blob/master/Screenshot%20from%202019-10-30%2009-25-46.png?raw=true" height = "400px">

### LICENSE
[MIT](https://github.com/MungaiKeren/E-Hood/blob/master/LICENSE)