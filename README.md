# Fastapi-tdd

Developing and Testing an Asynchronous API with FastAPI and Pytest

### _Dependencies_

1. FastAPI
2. Docker
3. Python
4. pytest

## Objectives

1. Develop an asynchronous RESTful API with Python and FastAPI
2. Practice Test-driven Development
3. Test a FastAPI app with pytest
4. Interact with a Postgres database asynchronously
5. Containerize FastAPI and Postgres inside a Docker container
6. Parameterize test functions and mock functionality in tests with pytest
7. Document a RESTful API with Swagger/OpenAPI

## Project structure

```
.
├── docker-compose.yml
├── LICENSE
├── README.md
└── src
    ├── app
    │   ├── core
    │   │   ├── create_app.py
    │   │   ├── docs
    │   │   │   ├── __init__.py
    │   │   │   ├── __pycache__
    │   │   │   │   └── __init__.cpython-310.pyc
    │   │   │   └── templates
    │   │   │       └── docs.html
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── create_app.cpython-310.pyc
    │   │   │   ├── __init__.cpython-310.pyc
    │   │   │   └── settings.cpython-310.pyc
    │   │   └── settings.py
    │   ├── __init__.py
    │   ├── main.py
    │   ├── posts
    │   └── __pycache__
    │       └── main.cpython-310.pyc
    ├── requirements.txt
    ├── tests
    └── venv
        └── include

```
