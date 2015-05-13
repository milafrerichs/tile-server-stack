# TileStache Server for Nepal Recovery Project

## Stack
- TileStache
- nginx
- gunicorn
- haproxy
- Docker

We're using Docker for easy deployments.

## Deployment

### Machine
Use [docker-machine](https://docs.docker.com/machine/) to deploy to AWS or DigitalOcean.
Steps:

#### Create new Machine
create a new machine with
```shell
docker-machine create
```
#### Activate new Machine (use docker in remote environment)
activate the remove environment with
```shell
eval "$(docker-machine env your-machine-name)"
```
### Compose
Use [Docker Compose]() to create a new docker setup.
Use the `production.yml` for deployment.

Steps:
#### Building
build your new docker containers (needed since nginx is a local docker container) with
```shell
docker-compose -f production.yml build
```

#### Scale
```shell
docker-compose -f production.yml scale app=3
```

#### Run
```shell
docker-compose -f production.yml up -d
```
`-d` ensures the container is run as a deamon
Check your deplyoment with `docker ps`

## Development

### Compose
Use [Docker Compose]() to create a new docker setup.

Steps:
#### Building
build your new docker containers with
```shell
docker-compose build
```

#### Scale
```shell
docker-compose scale app=3
```

#### Run
```shell
docker-compose up -d
```
