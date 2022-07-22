## github-repositories

This application is an exercise that will search the most relevant github repositories in C, Elixir, Python, PHP and Rust languages.

For the *Backend* we used [Django](https://www.djangoproject.com/), which is a popular [Python](https://www.python.org/) web framework, while Frontend uses HTML and pure CSS. *Data persistence* was built into a [PostgreSQL](https://www.postgresql.org) *database*, all in a development environment running on top of [Docker](https://www.docker.com).

## Installation

*Note: The following example commands assume the use of a Debian-based Linux operating system such as Ubuntu.*

The tools needed to build the application locally are **Python 3** with **Pip** and **Venv**, **Git** and **Docker**.

```console
sudo apt install -y python3 python3-pip python3-venv git docker docker-compose
```

Use Git to download the project from the repository

```console
git clone https://github.com/ali55on/github-repositories.git
```

Run the install script

```console
cd github-repositories/ && sudo sh install.sh
```

🎉 Finished!

To test, just run the app with `start-app` script, and access the address [127.0.0.1:8000](http://127.0.0.1:8000/) in your browser.

```console
./start-app
```

## Tests

Activate the virtual environment

```console
. venv/bin/activate && cd gittools/
```

Run the tests

```console
python manage.py test searchapp
```

A test coverage report can be done with Coverage tool

```console
coverage run --source='.' manage.py test searchapp && coverage report
```
