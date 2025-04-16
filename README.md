# Kudos App

A simple application to send and receive kudos within an organization.

## Backend (Django)

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

## Frontend (React)

### Prerequisites

- Node.js 18+
- pnpm

### Setup

1. Navigate to the frontend directory:

```bash
cd frontend
```

2. Install dependencies:

```bash
pnpm install
```

3. Start the development server:

```bash
pnpm dev
```

## API Authentication

- Use the `/api/login` endpoint to get a JWT token.
- Include the token in the `Authorization` header as `Bearer <token>` for authenticated requests.

## Notes

- The project uses SQLite for local development.
- You can manually seed users or organizations from the Django admin or with scripts.

