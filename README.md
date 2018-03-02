# N-Tier Stack Example
This repository represents a collection of docker files and
the required source code for the deployment and hosting of 
a basic web app which is integrated with a proxy (NGINX) and 
a backend database, in this case PostgreSQL.

## Architecture

The overall architecture that is contained within the docker
deployment can be seen below

<insert-image-reference-here>


## Components
The stack is comprised of the following components, which 
have been chosen for their familiarity and easey/quick stand
up time.

### NGINX

### Django

### PostgreSQL


# Landing Page

<insert-landing-page-screenshot-here>



# Getting started
The instructions for getting the stack up and running 
can be found below. Some things to consider for a successful
replication of this stack in a new environment are summarised
as well. 
## Environment
The stack was developed and tested in the following environment
* macOS High Sierra, version 10.13.3
* docker-compose version 1.18.0, build 8dd22a9
* docker version 17.12.0-ce, build c97c6d6


## Clone
First steps will be to pull this repo and change into the repositories
root directory with the following commands:
```bash
git clone https://github.com/castlemilk/demo1
cd demo1
```

## Build the stack [OPTIONAL]
This will carry out the steps to freshly build all of the 
docker images used/developed for this stack. Alternatively,
if this step is skipped, then we'll be using docker images
hosted on [docker hub](<insert-hub-link>)
```bash
docker-compose build
```
## Start the stack
This will execute the available docker-compose.yml file, carrying 
out all the steps to create our multi-tiered architecture,
and initialising all the containers with their required data
and configuration.
```bash
docker-compose up -d
```

## check/validate the stack
Once the stack is up and running (hopefully without issues), we can
check the status of the stack via:
```bash
docker ps | grep demo
```
Or
```bash
docker-compose top
```

## view the output of the stack
Assuming there's no issues binding to port 80 on localhost, it 
should be possible to browse to:

[localhost](http://localhost)


# Example of what you should see

<insert-example-of-what-you-should-see>
