***
## About the project:
In this project we created a simple customer registration form which using Django Web Framework. The project using Sqlite 3 database to keep and manipulate the customer informations. These informations are name, surname, TC number, phone number, city, district, registration date and (auto created by sqlite 3) id number. In the project user can add new customers to the database, change an existing customer's information or delete a registered customer. In main page user can access details of each customer's information. In addition, customers can be searched by their names, surnames, TC numbers, phone numbers, cities or districts.
***
## Project built with:
### Backend:
* Python
* Django
* Sqlite 3
### Frontend:
* Html 5
* CSS
* Bootstrap 4.5
***
## Installation
1. Clone The Repository
2. Install Django 3.2.6
3. Database Process

* CREATE DATABASE project_db_name
* CREATE USER projectuser WITH PASSWORD 'password';
* GRANT ALL PRIVILEGES ON DATABASE project_db_name TO projectuser
* After that define your database informations to setting.py or environ file.

4. Create Database

* python manage.py makemigrations
* python manage.py migrate

5. Create User For Project
* python manage.py createsuperuser
* After than you can define your username and password.

6. Run project
* python manage.py runserver