# Cookiecutter Pathway

Powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter), Cookiecutter Pathway is a framework for jumpstarting
production-ready Pathway projects quickly.

## Features

- Works with Python 3.11
- Generates runnable Python project both in batch and streaming mode
- [12-Factor](http://12factor.net/) based settings via [pydantic](https://docs.pydantic.dev/latest/usage/settings/) and [python-dotenv](https://github.com/theskumar/python-dotenv)
- Optimized development and production settings
- Comes with sample application ready to go
- Choose between kafka and redpanda for production
- Docker support using [docker-compose](https://github.com/docker/compose) for development and production
- Run tests with pytest

## Usage

First, get Cookiecutter.

    $ pip install "cookiecutter>=1.7.0"

Now run it against this repo:

    $ cookiecutter https://github.com/pathwaycom/cookiecutter-pathway

You'll be prompted for some values. Provide them, then a Pathway project will be created for you.
Enter the generated directory, read the README.md and start developing!
