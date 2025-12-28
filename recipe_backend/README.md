# Recipe Management API

A simple FastAPI backend for managing recipes with SQLite database.

## Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `POST /recipes` - Create a new recipe
- `GET /recipes` - List all recipes
- `GET /recipes/{id}` - Get a specific recipe
- `PUT /recipes/{id}` - Update a recipe
- `DELETE /recipes/{id}` - Delete a recipe

## Running locally

```bash
cd recipe_backend
poetry install
poetry run fastapi dev app/main.py
```

## Environment Variables

- `DATABASE_PATH` - Path to SQLite database file (default: `/data/app.db`)
