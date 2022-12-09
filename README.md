# CODE CHALLENGE MOSANO

Mosano Code Challenge.

## GETTING STARTED

This projects is an API platform based on Python and Django to provide data on Game of Thrones.

An application that can show the great houses of the Seven Kingdoms with a few members. The data available are:
* Houses (only the great houses)
* Members (some character on each great house)

You can check the data source [here](https://awoiaf.westeros.org/index.php/List_of_Houses#Great_Houses).

## INSTALL & CONFIGURE

Prerequisites (dev):
* [install pyenv and configure python](https://github.com/pyenv/pyenv)
* [docker and docker-compose](https://docs.docker.com/engine/install/ubuntu/)
* [install Postman to test it in details](https://www.postman.com/)

Run dockerly:

```shell
docker compose down && docker compose up -d
docker compose logs -f
```

In the first time running, please insert the data on database and create an admin superuser to manage the api:

```shell
$ poetry run python ./scripts/insert_dataset.py
$ sudo docker exec -it got_api /bin/sh
/app $ poetry run python manage.py createsuperuser
```

Prerequisites (production):
* [configure ssh and gitlab environment](https://docs.gitlab.com/ee/ci/environments/)
* [docker and docker-compose](https://docs.docker.com/engine/install/ubuntu/)

Run dockerly:

```shell
docker compose down && docker compose up -d
```

## DEVELOPER'S GUIDE

You can consume this api by generating a token or a JWT token on EPs:
* api/v1/auth/login/
* api/v1/access/token/
* api/v1/sliding/stoken/

Look at the details of this api and its resources on EPs:
* /api/v1/swagger/
* /api/v1/doc/
* /api/v1/redoc/

After it, you can call the CRUD's EPs to test it:
* /api/v1/got/houses/
* /api/v1/got/members/
or you can try out test it on:
* /api/v1/doc/
* /api/v1/redoc/

Any doubt, please check on documentation and/or contact me (alves.engleandro@gmail.com).

## QUALITY STANDARDS

Not available yet.
