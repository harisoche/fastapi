# fastapi

## Swagger
  - http://127.0.0.1:8000/docs or http://localhost:8000/docs

How to run apps:
```sh
1. pip install -r requirement.txt.
2. generate migration.
3. run apps via terminal `uvicorn app.main:app --reload` or `uvicorn app.main:app --reload --port 1357` if you want use custom port.
```

How to generate migration:

```sh
# alembic init via terminal
alembic init -t async app/migrations

# generate migration file
alembic revision --autogenerate -m "migrate database"

# apply all migration
alembic upgrade head
```
