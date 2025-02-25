# Lab 4 - Django and Flask

## Installations
- add that stuff
---
# Starting Django Project
First I created the project called stevens, using the lines below.
![project start](https://github.com/user-attachments/assets/b8e2ea14-2bd5-413e-904a-ad4790c71e56)

## Starting Django App
Next I create an app called my app in the same directory.
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

![copying urls.py](https://github.com/user-attachments/assets/4523b23c-eb14-4a1a-915a-a5bca0518c9c)

![copying admin.py, models.py, views.py](https://github.com/user-attachments/assets/716cc9fe-2585-496d-969c-8ee9306eea4c)

## Copying index.html
Similarly I created the necessary directories and copyed the index.html files using the lines shown below.

![copying index.html](https://github.com/user-attachments/assets/e731ba25-c134-4adc-b92b-61a08345a725)

## Setting up Google Maps API
First I had to create an account on the Google Maps Platform to generate an API key. Without this, it wouldnt be possible to use the Google Maps API. After creating the key, I used ```nano index.html``` and edited the API key parameter.

## Copying Static Files
![copying static files](https://github.com/user-attachments/assets/1aea94fd-7d73-47c1-a5df-1fb60a7b54c0)

## Creating Django Superuser
![creating superuser](https://github.com/user-attachments/assets/76a2ff53-4502-4739-8760-7aac229d960c)

## Run Django Server
![Running server](https://github.com/user-attachments/assets/52075b4d-c427-44a7-adfa-1730a1807e26)

## 
![Client Side](https://github.com/user-attachments/assets/3d25a79d-6011-4727-8ecb-9f82490efb24)


