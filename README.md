# Contact list

Web application to visualise contacts.
Users have 3 types of permission: read only, read and create, read, create and delete.

---

## Table of contents

1.  [ Installation ](#installation)
2.  [ Run ](#run)
3.  [ Support ](#support)

---


<a name="installation"></a>
## 1. Installation

1. ``` git clone  ```
2. ``` pip3 install -r requirements.txt ```

Here maybe appear a problem with mysqlclient
(```sudo apt-get install python3.*-dev libmysqlclient-dev ``` this helps me)


Also you need to install MySQL:
1. ``` sudo apt install mysql-server ```
2. ``` sudo mysql_secure_installation ```
3. then answer y (yes) for all questions
4. then create a password

Then you need create database in MySQL:
1. ``` sudo mysql ```
2. ``` ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'password'; (enter password: passWord1*) ```
or you need to change password in contact_list/project/project/settings.py (78 line)

3. ``` CREATE DATABASE db_contacts_and_users; ```
4. ``` exit ```


Then to send message to email you need to put your credintials to contact_list/project/project/settings.py  (lines 119-122).

---

<a name="run"></a>
## 3. Run

Migrations:

1. ```python3 manage.py makemigrations ```
2. ```python3 manage.py migrate ```


To fill the database:

 ``` python3 manage.py shell < create_test_db.py ``` - to create database with data for testing code

To launch app:
 ``` python3 manage.py runserver ```

If you want to read only, you need login with:
    login: User1
    password: 111
to read and create:
    login: User2
    password: 222
to read, create and delete:
    login: User3
    password: 333

---

<a name="support"></a>
## 4. Support

You can text me.

- Email at - strashko.elena.a@gmail.com.


---


