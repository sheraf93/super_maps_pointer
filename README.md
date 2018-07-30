# super_maps_pointer

Super maps pointer is yet another game intended to upgrade for geography skills while having fun :D

## With what technologies?

* Python version 3.6

### Backend

Using [Flask](http://flask.pocoo.org/) the python microframework.

#### Note:

For pythonista and developers, a `Pipfile` have been used instead of `requirements.txt` and `venv`.
Therefore, to install new packages, one need to use `pipenv install <package>` instead of `pip install <package>`.

### Frontend (Not setup yet)

* [AngularJS](https://angularjs.org/)
* D3.JS

## Requierments

* Docker

* Docker-compose

### Setup

Clone this repository.
This app is running with `Docker`. First install it (It has been tested on UNIX and Windows env).

In order to run the app, launch the following command:

### Initialize volume and databases

```bash
docker-compose up -d
```

#### Run the app

```bash
docker-compose up
```

Then please go to [localhost:5000](127.0.0.1:5000)

## Can I play online?

Not yet, but the project will be hosted by `heroku` once it will be mature enough according to the dev team

### Can I help?

Yes! If you have any tech advice please contact us or create an issue!
