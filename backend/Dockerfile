FROM python:3.6

LABEL maintainer "chretien.max@gmail.com"

# -- Install Pipenv:
RUN pip3 install pipenv

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# -- Install Application into container:
RUN set -ex && mkdir -p /super_maps_pointer/backend

WORKDIR /super_maps_pointer/backend

# -- Adding Pipfiles
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

# -- Install dependencies:
RUN set -ex && pipenv install --deploy --system --ignore-pipfile

EXPOSE 8000/tcp

# -- Run flask:
CMD flask run -h 0.0.0.0 -p 8000 --no-debugger --no-reload
