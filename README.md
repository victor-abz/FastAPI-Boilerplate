## Installation

```shell
$ python3.9 -m venv venv
$ source venv/bin/activate
$ export PYTHONPATH=$PWD
$ pip install -r requirements.txt
```

## Getting Started
 
### 1. Setup Env variable
 Create `.env` file at root of project based on ennv_example provided

### 2. Start Application
```shell
$ python main.py
```
the app will be listening to specified port in  `.env`

## API Documentation
Swagger Documentation at `/docs` when app running.  

## Folder structure

- `app:` priority folder of all your application related code.
    - `controllers:` Business Logic.
    - `database:` Contain all the database logic.
        - `models:` Data Base and ML/DL models related backbone code
        - `baseclass.py:` Add models base itesm(Shared across other models)
        - `base.py:` Import all your models here.
        - `__init__.py:` Database session
     - `routes:` Your App routing
    - `schemas:` Database schema used for validating user input
    - `utils:` Contain all the utilities.
    - `config.py:` Get congis values
    - `initializer.py:` Routes prefixes (Add your routes here)
- `.env:`  Application settings
- `main.py:` Abstract Uvicorn start command -- Execute this to start App
- `manage.py:` App Entry point
- `requirements.txt:` Application dependencies