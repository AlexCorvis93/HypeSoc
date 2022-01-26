# Hype
Description:

This is test-project of a mini social network for demonstration my programming skills.

## How to start a dev environment

Prerequisites:

* Python 3.9 
* Postgres 
* Django REST-framework

#Manual installation
First step for Linux(update Python, installation pip, postgresql and virtual environment):
* sudo apt update
* sudo apt -y upgrade
* sudo apt install -y python3-pip
* sudo apt install -y python3-venv
* sudo apt -y install postgresql


create work directory and clone repository:

* :~$ cd home/user/Projects/
* :~$ mkdir Hype/
* git clone github.com/AlexCorvis93/HypeSoc.git

Create DATABASE postgres:

Enter in postgres:
sudo -u postgres psql
*      CREATE DATABASE hype;
*     CREATE USER myuser WITH PASSWORD 'password';
*      ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
*     ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed'
*      ALTER ROLE myprojectuser SET timezone TO 'UTC';
*     GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;

Exit: \q

CREATE VIRTUAL ENVIRONMENT:
* python3 -m venv venv
* source env/bin/activate

Example: (env) user@user-System-Product-Name:~/Hype$

Installation dependencies:
* pip install -r requirements.txt

Don`t forget change setting.py and create '.env'  for secrets items

Example for '.env':

          SECRET_KEY=writeanydjangosettingskey
          DB_NAME=hype
          DB_USER=databaseuser
          DB_PASS=yourpassword
          DEBUG=True

SETTING PROJECT:

* ~/myprojectdir/manage.py makemigrations
* ~/myprojectdir/manage.py migrate
* python manage.py createsuperuser


# Manual Deploy to the VPS
connecting to the server:

       ssh root@<ip adress>     
       password: some password

1. UPGRADE packages on server
    
       sudo apt update
       sudo apt upgrade

2. INSTALLATION NECESSARY SOFT
   
        sudo apt install python3-pip python3-dev nginx postgresql postgresql-contrib curl

3. CREATE USER and login

       adduser user_name
       usermod -aG sudo user_name
       usermod -aG www-data user_name
       su - user_name


4. CREATE DATABASE
    
        sudo -u postgres psql
        CREATE DATABASE <name>;
        CREATE USER username WITH PASSWORD 'password';
        
   ADJUSTMENT DATABASE:
    
             ALTER ROLE username SET client_encoding TO 'utf8';
             ALTER ROLE username SET default_transaction_isolation TO 'read committed';
             ALTER ROLE username SET timezone TO 'UTC';
             GRANT ALL PRIVILEGES ON DATABASE myproject TO username;
             \q



5. GO TO THE WORK FOLDER
         
       cd /home/user_name/

6. COPY THE REPOSITORY

         git clone repository_name

7. ENTER access TOKEN FROM GITHUB

8. INSTALL VIRTUAL ENVIRONMENT and ACTIVATE
          
       python3 -V
       sudo apt install python3.8-venv
       python3 -m venv venv
       source venv/bin/activate


9. INSTALL GUNICORN

        pip install django gunicorn psycopg2-binary

10. INSTALL REQUIREMENTS

        pip install -r requirements.txt

11. CREATE MIGRATIONS

        python manage.py makemigrations
        python manage.py migrate

12. STATIC

         python manage.py collectstatic

13. CREATE SUPERUSER

          python manage.py createsuperuser


14. CHECK GUNICORN and exit from venv

           gunicorn --bind <server ip adress>:8000 hype.wsgi
           deactivate

15. CREATE SOCKET FILE GUNICORN

            sudo nano /etc/systemd/system/gunicorn.socket
            
        PASTE it in the file:
            [Unit]
            Description=gunicorn socket

            [Socket]
            ListenStream=/run/gunicorn.sock

            [Install]
            WantedBy=sockets.target

16. CREATE GUNICORN SERVICE FILE
            
         sudo nano /etc/systemd/system/gunicorn.service

         PASTE it in the file:

           [Unit]
           Description=gunicorn daemon
           Requires=gunicorn.socket
           After=network.target

           [Service]
           User=<username>
           Group=www-data
           WorkingDirectory=/home/useername/Hype
           ExecStart=/home/username/Hype/venv/bin/gunicorn \
           --access-logfile - \
           --workers 3 \
           --bind unix:/run/gunicorn.sock \
           hype.wsgi:application

             [Install]
             WantedBy=multi-user.target

17. ACTIVATE SOCKET and CHECK

         sudo systemctl start gunicorn.socket
         sudo systemctl enable gunicorn.socket
         sudo systemctl status gunicorn.socket

18. TESTING CURL

          curl --unix-socket /run/gunicorn.sock localhost


19. ADJUSTMENT NGINX

CREATE FILE:
            
       sudo nano /etc/nginx/sites-available/hype

PASTE IT:
 
    server {
    listen 80;
    server_name server_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/username/hype;
    }
    location /media/ {
        root /home/username/hype;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
    }

CREATE LINK TO THE SITES-ENABLED CATALOG:

    sudo ln -s /etc/nginx/sites-available/hype /etc/nginx/sites-enabled

RESTART NGINX:
 
     sudo systemctl restart nginx



