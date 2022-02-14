# Django React Boilerplate

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](code_of_conduct.md)
[![License: MIT](https://img.shields.io/github/license/vintasoftware/django-react-boilerplate.svg)](LICENSE.txt)

## About
A [Django](https://www.djangoproject.com/) project boilerplate/template with lots of state of the art libraries and tools like:
- [React](https://facebook.github.io/react/), for building interactive UIs
- [django-js-reverse](https://github.com/ierror/django-js-reverse), for generating URLs on JS
- [React Bootstrap](https://react-bootstrap.github.io/), for responsive styling
- [Webpack](https://webpack.js.org/), for bundling static assets
- [Celery](https://docs.celeryproject.org/), for background worker tasks
- [WhiteNoise](http://whitenoise.evans.io/en/stable/) with [brotlipy](https://github.com/python-hyper/brotlipy), for efficient static files serving
- [prospector](https://prospector.landscape.io/en/master/) and [ESLint](https://eslint.org/) with [pre-commit](https://pre-commit.com/) for automated quality assurance (does not replace proper testing!)

For continuous integration, a [Github Action](https://github.com/features/actions) configuration `.github/workflows/main.yml` is included.

Also, includes a Heroku `app.json` and a working Django `production.py` settings, enabling easy deployments with ['Deploy to Heroku' button](https://devcenter.heroku.com/articles/heroku-button). Those Heroku plugins are included in `app.json`:
- PostgreSQL, for DB
- Redis, for Celery
- Sendgrid, for e-mail sending
- Papertrail, for logs and platform errors alerts (must set them manually)

This is a good starting point for modern Python/JavaScript web projects.

## Running
### Tools
- Setup [editorconfig](http://editorconfig.org/), [prospector](https://prospector.landscape.io/en/master/) and [ESLint](http://eslint.org/) in the text editor you will use to develop.

### Setup
- Inside the `backend` folder, do the following:
  - Create a copy of `psql_jupyter/settings/local.py.example`:  
  `cp psql_jupyter/settings/local.py.example psql_jupyter/settings/local.py`
  - Create a copy of `.env.example`:
  `cp .env.example .env`

### If you are using Docker:
- Open the `/backend/.env` file on a text editor and uncomment the line `DATABASE_URL=postgres://psql_jupyter:password@db:5432/psql_jupyter`
- Open a new command line window and go to the project's directory
- Run the initial setup:
  `make docker_setup`
- Create the migrations for `users` app:  
  `make docker_makemigrations`
- Run the migrations:
  `make docker_migrate`
- Run the project:
  `make docker_jupyter`
- While the project is running, you can also run `make docker_createsuperuser` to create a superuser for your DB
- Open the URL that will be displayed on the console
  - Inside the Jupyter notebook interface, go to the `notebooks/` dir and click on `New`. In the dropdown, click on `Django Shell-Plus`
  - You can also toy around with the `test.ipynb` that comes pre-made
- To stop the project, run:
  `make docker_down`

#### Adding new dependencies
- Open a new command line window and go to the project's directory
- Update the dependencies management files by performing any number of the following steps:
  - To add a new **frontend** dependency, run `npm install <package name> --save`
    > The above command will update your `package.json`, but won't make the change effective inside the container yet
  - To add a new **backend** dependency, update `requirements.in` or `dev-requirements.in` with the newest requirements
- After updating the desired file(s), run `make docker_update_dependencies` to update the containers with the new dependencies
  > The above command will stop and re-build the containers in order to make the new dependencies effective

## Linting
- Manually with `prospector` and `npm run lint` on project root.
- During development with an editor compatible with prospector and ESLint.

## Pre-commit hooks
- Run `pre-commit install` to enable the hook into your git repo. The hook will run automatically for each commit.
- Run `git commit -m "Your message" -n` to skip the hook if you need.

## Contributing

If you wish to contribute to this project, please first discuss the change you wish to make via an [issue](https://github.com/vintasoftware/django-react-boilerplate/issues).

Check our [contributing guide](https://github.com/vintasoftware/django-react-boilerplate/blob/master/CONTRIBUTING.md) to learn more about our development process and how you can test your changes to the boilerplate.

## Commercial Support
This project, as other Vinta open-source projects, is used in products of Vinta clients. We are always looking for exciting work, so if you need any commercial support, feel free to get in touch: contact@vinta.com.br

Copyright (c) 2021 Vinta Serviços e Soluções Tecnológicas Ltda.

[MIT License](LICENSE.txt)
