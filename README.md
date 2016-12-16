# Vagrant-Django
Vagrant + Django (No known issues)

This machine contains: MySQL, Apache, PHP, Python, Django-cms and Nodejs
How to setup:

    git clone https://github.com/Externoak/Vagrant-Django.git

    cd Vagrant-Django

    Vagrant up

    Vagrant ssh

    cd django-cms

    source bin/activate

W/O Quotes.

    django-admin.py startproject “Name of your Project”

    cd “Name of your Project”
    
    sudo python manage.py migrate
    
    sudo python manage.py runserver “IP:PORT”

Allowhost error:
    If your'e getting Allowhost error you must modify the following.
          
           sudo nano “Name of your Project”/settings.py
                Modify ALLOWED_HOSTS = ['"Your IP"']
