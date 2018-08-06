# BACKEND

Using [Flask](http://flask.pocoo.org/) the python microframework.

* With Python version 3.6

## Database

* postgreSQL using [SQLAlchemy](https://www.sqlalchemy.org/) version 1.2.10

## Developper Setup

A `Pipfile` have been used instead of old `requirements.txt` and `venv`.
Therefore, to install new packages, one need to use `pipenv install <package>` instead of `pip install <package>`.

1. Make sure you have python 3.6 installed on your machine
2. Install pipenv

In backend folder, uses
```bash
pip3 install pipenv
```

That's it. after installing or removing a package using `Pipenv`, just relaunch the `docker-compose up` command from repository root `super_maps_pointer` folder.

### Debugger

A debugger called: `Python: Attach debugger` is set up with **VS Code**, to use it:

1. launch the app with `docker-compose up`.
2. set any breakpoints you need.
3. launch the debugger.

## Unit Tests

Soon