# Hype

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









