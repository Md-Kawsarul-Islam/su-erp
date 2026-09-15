# SU ERP

Flutter Web frontend + Django REST API backend for the SU ERP system.

## Production architecture

- GitHub: source code
- Render: Django API + PostgreSQL
- Vercel: Flutter Web frontend

## Local backend

```bash
cd backend
python -m venv venv
# Windows: venv\\Scripts\\activate
pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
python manage.py runserver
```

## Local frontend

```bash
cd frontend
flutter pub get
flutter run -d chrome
```

## Production frontend API URL

The API URL is injected at build time:

```bash
flutter build web --release --dart-define=API_BASE_URL=https://YOUR-RENDER-SERVICE.onrender.com
```

## Render

The included `render.yaml` can be used as a starting point. After deployment, set:

- `ALLOWED_HOSTS` to the Render API hostname
- `CORS_ALLOWED_ORIGINS` to the exact Vercel frontend URL
- `CSRF_TRUSTED_ORIGINS` to the exact HTTPS frontend/admin origins if needed

Render's `DATABASE_URL` is used automatically when present.

## Vercel

The GitHub Actions workflow builds Flutter Web and deploys `frontend/build/web` to Vercel.
Add these GitHub repository secrets:

- `API_BASE_URL` = your Render API URL
- `VERCEL_TOKEN` = your Vercel token

Push to `main` to trigger the frontend deployment.

## Security

Never commit `.env`, database passwords, Django secret keys, local SQLite databases, virtual environments, or build artifacts.
