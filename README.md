# QA_System
Is an application API were users can post questions with attachment to Mentor, Mentors can see the list of questions and answer the questions.<br />
Tech stack - Python 3.8 | Django | Django REST

# Getting Started

### Install Python

#### Linux
Most UNIX systems come with a python3 interpreter pre-installed.

#### Windows
[Python Setup on Windows](https://docs.python.org/3/using/windows.html)

### Install Pip
```console
developer@ubuntu:~$ sudo apt install -y python3-pip
```
### Setting Up a Virtual Environment
```console
developer@ubuntu:~$ sudo apt install -y python3-venv
```
### Create and Activate env
```console
developer@ubuntu:~$ python3 -m venv qa_env
developer@ubuntu:~$ source qa_env/bin/activate
```
### Install packages
Once the qa_env is actiavted we can install the packages
```console
(qa_env) developer@ubuntu:~$ pip install -r requirements.txt
```
### Database
We are using django default sqlite3 database

### Run the development server
```console
developer@ubuntu:~$qa_system/mahvie python manage.py migrate
developer@ubuntu:~$qa_system/mahvie python manage.py runserver
```
