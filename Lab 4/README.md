# Lab 4 - Django and Flask

## Overview
This lab contained three sections: running the Django project, running the Django REST project, and running the flask server. These tasks teach you how to setup and run projects using the Django package, use API keys to include API services within a project, and run servers using the Flask package.

## Installations
The following commands can be used to install the necessary packages to run the Django and Django REST projects, as well as Flask to run the Flask server.
```console
pip install -U setuptools
pip install -U django
pip install -U djangorestframework
pip install -U django-filter
pip install -U markdown
pip install -U requests
pip install -U flask
```

## Table of Contents
1. [Django Project Stevens](#django-project---stevens)
2. [Djange REST Project - MyCPU](#django-rest-project---mycpu)
3. [Flask Server](#flask-server)
---
# Django Project - Stevens
## Starting Django Project
First I created the project called stevens, using the lines below.

![project start](https://github.com/user-attachments/assets/b8e2ea14-2bd5-413e-904a-ad4790c71e56)

## Starting Django App
Next I create an app called myapp in the same directory.

![app start](https://github.com/user-attachments/assets/328224a7-fb27-4be9-a21d-eab07bf9c519)

## Setting up SQLite Database
Since I am using a Windows machine, I am using the default, SQLite. I used ```python manage.py migrate``` to create the SQLite database.

![migrate output](https://github.com/user-attachments/assets/520f1e9e-d022-4819-a81b-0dbf47f75215)

## Editing settings.py
In order to properly setup the project, certain sections in the settings file must be changed. I used ```nano settings.py``` to add an asterisk in the ALLOWED_HOSTS variables. The INSTALLED_APPS list should include my_app at the end, with the comma. Finally, I changed the timezone to "America\New_York" to show the correct time.

![allowed hosts change](https://github.com/user-attachments/assets/eb32e9b7-6f5e-44f9-9d37-3d68db0e9af8)\
![add my app](https://github.com/user-attachments/assets/63ff9cd3-6b72-46ec-a421-16450395b116)\
![change timezone](https://github.com/user-attachments/assets/607f3821-b9e3-4c2f-9ae8-652c9e8408c1)

## Copying urls.py, admin.py, models.py, views.py
I copyed urls.py to the stevens directory, and admin.py, models.py, and views.py to the myapp directory using the lines shown below.

![copying urls.py](https://github.com/user-attachments/assets/4523b23c-eb14-4a1a-915a-a5bca0518c9c)\
![copying admin.py, models.py, views.py](https://github.com/user-attachments/assets/716cc9fe-2585-496d-969c-8ee9306eea4c)

## Copying index.html
Similarly I created the necessary directories and copyed the index.html files using the lines shown below.

![copying index.html](https://github.com/user-attachments/assets/e731ba25-c134-4adc-b92b-61a08345a725)

## Setting up Google Maps API
First I had to create an account on the Google Maps Platform to generate an API key. Without this, it wouldnt be possible to use the Google Maps API. After creating the key, I used ```nano index.html``` and edited the API key parameter.

## Copying Static Files
In order to properly display the website, I copied the rest of the remaining files.

![copying static files](https://github.com/user-attachments/assets/1aea94fd-7d73-47c1-a5df-1fb60a7b54c0)

## Creating Django Superuser
In order to become an admin on the server that I am running, I need to establish myself as a superuser. Initially the line, ```python3 manage.py createsuperuser``` did not work, but this was fixed by using ```winpty python3 manage.py createsuperuser```. Then I entered my credentials and created an account.

![creating superuser](https://github.com/user-attachments/assets/76a2ff53-4502-4739-8760-7aac229d960c)

## Run Django Server
Now that everything has been setup, I ran the server using ```python3 manage.py runserver```. I opened the app as an admin by going to http://127.0.0.1:8000/admin. From there, I entered the necessary data, including the date and time, temperature, and location.

![Running server](https://github.com/user-attachments/assets/52075b4d-c427-44a7-adfa-1730a1807e26)

## Client View
To see this from the client side, I went to http://127.0.0.1:8000, and you can see the data that I entered being displayed.

![Client Side](https://github.com/user-attachments/assets/3d25a79d-6011-4727-8ecb-9f82490efb24)

---

# Django REST Project - MyCPU
## Starting Django REST Project
Similarly to before, I created a Django project called mycpu.

![starting mycpu](https://github.com/user-attachments/assets/7505fa2d-d52b-4103-9107-f5b622fefc82)

## Starting Django App
Using the commands below, I created an app called myapp.

![Starting app](https://github.com/user-attachments/assets/aaf028de-f9ed-49d6-9838-41ab62668dde)

## Editing settings.py
Again, I needed to edit settings.py using ```nano settings.py```. I changed ALLOWED_HOSTS to have an asterisk, added myapp and rest_framework to INSTALLED_APPS, and changed the timezone to New York.

![change allowed hosts](https://github.com/user-attachments/assets/c2f726fb-6230-4829-b2c8-4919ea4091a5)\
![change installed apps](https://github.com/user-attachments/assets/e393e4d2-0d87-4ef0-b987-8e0253d6c949)\
![change timezone](https://github.com/user-attachments/assets/4e20a452-c56e-420a-ae71-a70382b5168d)

## Copying urls.py, admin.py, views.py, models.py, and serializers.py
I copied urls.py to the mycpu directory, and admin.py, views.py, models.py, and serializers.py to the myapp directory.

![copying files](https://github.com/user-attachments/assets/6a048c65-e1c0-49c0-bf4a-df014a2134b0)

## Edit password in views.py
I used ```nano views.py``` to change the default password of admin to something more secure.

## Copy index.html
I created the proper subdirectories and copied index.html by using the commands shown below.

![copying index.html](https://github.com/user-attachments/assets/0271508b-b5c6-4626-9ee2-405b7f982ee7)

## Edit index.html to Include API Key
Since I already generated an API in the previous section, I reused the same key. I edited index.html by using ```nano index.html```.

## Copy Static Files
Similar to before, I needed to include all of the static files, the CSS and JavaScript files. I used the commands below to copy these files into the proper directories

![copying static files](https://github.com/user-attachments/assets/3d8a5cfd-7918-4b9a-8161-4578fffbbd72)

## Copy controller.py to ~/mycpu
Since this project uses the REST framework, it needs additional files, such as controller.py. After doing some research, I found that the main difference between Django and the Django REST framework, is that the REST framework separates the front end and the back end. The program controller.py is sending data to the server, allowing it to be displayed on the website.

![copying controller.py](https://github.com/user-attachments/assets/097d321d-e618-4bad-8fe9-d0ade05ccd0d)

## Edit Password in controller.py
In this file I changed the default passwork from admin to the same one I used previously in views.py. Again, I used ```nano controller.py``` to edit the file.

## Create Superuser
By the using the lines below, I finished setting up the server, and established myself as a superuser by entering my credentials.

![making superuser](https://github.com/user-attachments/assets/d798b058-6d3c-49b9-b2e1-bd8bc21aaa97)

## Run Django Server
In order to run the server, I used ```python3 manage.py runserver```. To finish setting up the server I opened http://127.0.0.1:8000/admin and entered the latitiude and longitude of Stevens, 40.7451 and -74.0255 respectively. Then I posted the following data to each link 2024 to http://127.0.0.1:8000/dt, 20 to http://127.0.0.1:8000/cpu, and 20 to http://127.0.0.1:8000/mem.

![run server](https://github.com/user-attachments/assets/dbeed171-cdc2-4810-a481-5a8ae9551cd5)

Then I opened another termianl window and ran the controller.py program.

![controller.py](https://github.com/user-attachments/assets/2f36964a-01f8-4e5e-84ff-bf495e7f31f8)

## Client View
When viewing the site at 127.0.0.1:8000/home, you can see the location I entered previously on the Google Maps display. Also, the information regarding my CPU being printed by controller.py is being display and continuously updated.

![client view](https://github.com/user-attachments/assets/b900ed0e-ce8e-49a9-8217-8d9f7ef33bbb)

---
# Flask Server
## Installing Flask
Since I did not have Flask installed, I used ```pip install flask``` to install the package.

![installing flask](https://github.com/user-attachments/assets/3a9a4345-8471-4d93-8693-bcbfbf24da15)

## Running Flask Server
To run the server, I simply changed directories and ran the hello_world.py file. To view the site, I went to http://127.0.0.1:500, which can be seen below.

![running server](https://github.com/user-attachments/assets/d5db4a13-6a65-4fa2-bf26-b26a58c1402c)

![client side](https://github.com/user-attachments/assets/56451a6b-2e29-4efc-80a9-e13fe95f6673)

---
I pledge my Honor that I have abided by the Stevens Honor System - _Ray Ringston_
