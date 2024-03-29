# Project Tracker
[![Django CI](https://github.com/madhvi-n/django-project-tracker/actions/workflows/django.yml/badge.svg)](https://github.com/madhvi-n/django-project-tracker/actions/workflows/django.yml)


A project management app based on Django

# Features
- Add projects
- Create project boards (one board is generated by default)
- Add board sections (3 sections by default - To do, In Progress, Done)
- Create task types (Default types: Task, Bug, Story)
- Tasks with sub tasks
- Link project to organizations [TODO]
- Project members [TODO]
- Assign tasks to other team members [TODO]


# Requirements
- Backend
    - Python 3.8+
    - virtualenv
    - WSL


# Installation

Clone the repository and enter the root directory
```
git clone https://github.com/madhvi-n/django-project-tracker.git
cd django-project-tracker
```


Create a virtual environment and activate it
```
virtualenv venv
source venv/bin/activate
```

Making sure your virtual environment is activated, install the dependencies using `pip`
```
pip install -r requirements.txt
```

After installing dependencies, migrate Django apps.(You will find the list of apps when you run the command `python manage.py runserver`)
```
python manage.py migrate
```

Create django/python superuser using
```
python manage.py createsuperuser
```

Finally start your Django server
```
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` or `localhost:8000` for running web server
Alternatively you can access the admin interface on `http://127.0.0.1:8000/admin/` or `localhost:8000/admin`

Access python shell
```
python manage.py shell
```


### Generating data using shell
```
from django.contrib.auth.models import User
from projects.models import Project

# When a project is created, it creates a board with 3 board sections by default [Todo, In progress and Done]

user = User.objects.get(id=1)
project = Project.objects.create(
    title="Test project",
    content="A very long text as the content here",
    user=user
)

# get todo board section
section = BoardSection.objects.get(project=project, title__icontains="Todo").first()

# Similar to board sections, 3 tasks types are created by default for each project
task_type = TaskType.objects.get(id=1)
task = Task.objects.create(
    board_section=section,
    summary="CRUD for tasks",
    description="Implementation of create, read, update and delete for Task model,
    reporter=user,
    assignee=user,
    type=task_type
)

```

# API documentation
- Visit `http://127.0.0.1:8000/swagger/` or `localhost:8000/swagger/` for Swagger documentation
- Visit `http://127.0.0.1:8000/redoc/` or `localhost:8000/redoc/` for Redoc documentation



#### Note: Django/Backend runs on WSL



## References

- [How to install Python3.8 on Ubuntu 18.04](https://linuxize.com/post/how-to-install-python-3-8-on-ubuntu-18-04/)
