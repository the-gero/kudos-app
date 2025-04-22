### Prerequisites

- Python 3.11+
- [Poetry](https://python-poetry.org/)

### Setup

1. Navigate to the backend directory:

```bash
cd backend
```

2. Install dependencies:

```bash
poetry install
```

3. Apply migrations:

```bash
poetry run python manage.py makemigrations
poetry run python manage.py migrate
```

4. Start the backend server:

```bash
poetry run python manage.py runserver
```