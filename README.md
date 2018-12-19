# Council-Administration-Website
This is a django website developed for Council Administration Purposes.

The website is hosted. You can take a look at it here - [Website link](darshandv.pythonanywhere.com)
### Steps to Reproduce
Before starting please make sure that you have following installed and working properly.
- Python - 3.6
- pip
- git

It is advised to use a virtualenv for every Django project you start. Thus make sure your virtual environment is up and running.
```
git clone https://github.com/darshandv/Council-Administration-Website.git
```
Then inside the directory with virtual environment activated run these commands in the terminal -
``` python
pip install requirements.txt
python manage.py migrate
python manage.py runserver
```

You can access the website at `localhost:8000` (or the port specified in the terminal) in any of your browser.
