# ghibli-back · [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/ChauffeurPrive/nestor-api/blob/master/LICENSE) [![Workflow](https://github.com/ChauffeurPrive/nestor-api/workflows/ci/badge.svg?branch=master)](https://github.com/ChauffeurPrive/nestor-api/actions?query=workflow%3Aci+branch%3Amaster) [![codecov](https://codecov.io/gh/ChauffeurPrive/nestor-api/branch/master/graph/badge.svg)](https://codecov.io/gh/ChauffeurPrive/nestor-api)
ghibli-back is an API that allows to list Ghibli films with people involved in it.

## Installing
The API uses Python 3.8 or above.
Dependencies are managed by [Pipenv](https://github.com/pypa/pipenv).

```bash
pipenv sync # Add --dev to also install dev dependencies
```

## Running the tests
```bash
pipenv run make test-all
```

## Serving the app on port 8001
```bash
GHIBLI_API_URL="https://ghibliapi.herokuapp.com" FLASK_APP='./ghibli/api/wsgi.py' pipenv run flask run --port 8001
```

## Configuration

> [Source](./nestor_api/config/config.py)

|                                        Key | Default                | Unit       | Comment                                                     |
| -----------------------------------------: | ---------------------- | ---------- | ----------------------------------------------------------- |
|                           `GHIBLI_API_URL` |                        |            | URL of Ghibli API                                           |
