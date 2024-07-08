# Deepchecks Task

> Deepchecks excercise

## Pre-requisites

No local pre-requisites should be needed apart from:

- [docker](https://docs.docker.com/engine/installation/)
- [docker compose](https://docs.docker.com/compose/)
- [openssl](https://www.openssl.org/) (generates local secrets)

The local setup uses **docker compose** to spin up all necessary services.
Make sure you have it installed and can connect to the **docker daemon**.

The `docker-compose.yml` file describes the setup of the containers.

## Containers and services

The list of the containers:

| Container | Description                                            |
| --------- | ------------------------------------------------------ |
| app       | [Django](https://www.djangoproject.com/) web framework |
| nginx     | [NGINX](http://nginx.org/) server                      |
| db        | [PostgreSQL](https://www.postgresql.org/)              |
| redis     |                                                        |
| worker    |                                                        |

All of the container definitions for development can be found in the `docker-compose.yml`.

## Run

### Build the app

Run in project directory:

```bash
make prepare
make build-server
make server-up
```

This will generate secrets (`.env` file) for the local instances,

Open your browser and access the `APP_URL` entry in `.env` file.

### Start the server

Run in project directory:

```bash
docker compose up app
```

This will start the application behind NGINX along with all dependencies.

### Upgrade dependencies

#### Check outdated dependencies

```bash
docker compose run --rm --no-deps app eval pip list --outdated
```

**WARNING** Update or add a new dependency implies to rebuild the container
to catch up the new version or the new library.

## License

> **Copyright 2023 Savana Tech**

[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)

Licensed under the Apache License, Version 2.0 (the **“License”**);
you may not use this file except in compliance with the **License**.

You may obtain a copy of the **License** at
<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software distributed
under the **License** is distributed on an **“AS IS”** BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

See the **License** for the specific language governing permissions and
limitations under the **License**.

## API Endpoints

### GET /interactions/upload

Return the list of all interaction

### POST /interactions/upload

Accepts the interaction csv file

### GET /interactions/alerts

Return all alerts
