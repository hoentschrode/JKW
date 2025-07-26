# JKW website template

## Development setup 
I'm using [devenv](https://devenv.sh/) as development environment.

Since devenv's automatic setup of the venv requirements isn't working, the requirements have to be installed manually, after shell was activated by 
```(bash)
pip install -r requirements/development.txt
```

Migrate database setup (this also creates a local sqlite database)
```(bash)
python manage.py migrate
```

Create superuser (backend admin)
```(bash)
python manage.py createsuperuser
```

Start development server:
```(bash)
python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
```
```(bash)
```
