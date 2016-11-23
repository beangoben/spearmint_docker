# Spearmint docker image

Wanna test out Bayesian Optimization with jupyter notebook support?

## What's included?

Docker files to test-out Spearmint PESM with Python 2 and 'Vanilla' Spearmint with Python 3.

The docker image is based off of <https://github.com/beangoben/pimp_jupyter>, a scientific jupyter notebook image with enabled nbextensions. Also included:

- MongoDB (+ pymongo)
- Spearmint PESM is from <https://github.com/HIPS/Spearmint/tree/PESM>
- Spearmint with python3 support is from <https://github.com/redst4r/Spearmint/tree/python3>
- Each version also has access to NLOPT <http://ab-initio.mit.edu/wiki/index.php/NLopt>
- There are two test scripts that show how to run for each version a simple Bayesian Optimization on branin

**Don't forget to read the license and cite the work!** (Check original githubs for more info)

## How to use

To run the software on any computer you need to install [docker](https://www.docker.com/).

Then you can either download or build the docker image.

### 1) Get image
#### Pull from dockerhub
To download running the following command in your favorite terminal:

```
docker pull beangoben/spearmint_docker
```
#### Build it locally
of build it (good to change things) by moving to the git cloned repository :

```
docker build -t "beangoben/spearmint_docker" .
```
### 2) Run image

#### As a jupyter notebook server
And then move to whatever folder you want to work with and execute:

```
docker run -p 8888:8888 -v "$(pwd)":/home/jovyan/work -it beangoben/spearmint_docker
```

#### As a executable script

You can also execute spearmint directly on your experiment folder "test_py2" using:


```
docker run -p 8888:8888 -v "$(pwd)":/home/jovyan/work -it beangoben/spearmint_docker start.sh ./experiment_py2.sh test_py2
```
