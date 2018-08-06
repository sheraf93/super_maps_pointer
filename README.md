# SUPER MAPS POINTER

Super maps pointer is yet another game intended to upgrade for geography skills :earth_africa: while having fun :smile:

### With what technologies?

* Flask version 1.0.2
* Angular version version 6.1.2

### Requierments

* Docker
* Docker-compose

## Setup

#### 1. Clone this repository. 

```bash
git clone https://github.com/sheraf93/super_maps_pointer.git
```

#### 2. Install Docker

This app is running with `Docker`. This [link] for how to install it.

#### 3. Initialize volume and databases using docker-compose

In order to Initialize volume and databases, launch the following command:

```bash
docker-compose up -d
```

Make sure you are in the root folder, because the file `docker-compose.yml` will use `Dockerfile`s in both backend and frontend folders.

### 4. Run the app

```bash
docker-compose up
```

If all containers are up without problems:
  - `super_maps_pointer_flask_app`
  - `super_maps_pointer_angular_app`
  - `postgres:10`

Then you can now starting using the app in [localhost:4200](http://127.0.0.1:4200)

**Note for windows users**: sometimes Docker for windows have trouble copying the files into the containers, most of the time you just have to restart Docker to make it work.

## Can I play online?

Not yet, but the project will be hosted by `heroku` once it will be mature enough according to the dev team.

**Note for devs**: There is already vscode folder for debugging the app in both backend and frontend folders. 

## Can I help?

Yes! If you have any tech advice please contact us or create an issue!
