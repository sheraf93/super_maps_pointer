FROM python:3.6

MAINTAINER kruupos <chretien.max@gmail.com>

# -- Install Pipenv:
RUN pip3 install pipenv

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# -- Install Application into container:
RUN set -ex && mkdir /super_maps_pointer

WORKDIR /super_maps_pointer

# -- Adding Pipfiles
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

# -- Install dependencies:
RUN set -ex && pipenv install --deploy --system --ignore-pipfile

# -- Run flask:
CMD flask run -h 0.0.0.0
