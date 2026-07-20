# Codex Commerce Django Website

A commercial Django website with business pages, services, products, pricing, testimonials, searchable blog, comments, newsletter subscriptions, contact messages, RSS, sitemap, and Django admin management.

## Quick Start

### Local Development (SQLite)

```powershell
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

### With Docker (PostgreSQL)

```powershell
docker-compose up -d
```

Then run migrations inside the container:

```powershell
docker exec wwt-django python manage.py migrate
docker exec wwt-django python manage.py seed_demo
```

Open `http://localhost:8000/` (Django), `http://localhost:5050/` (PgAdmin).

Demo admin credentials after seeding:

```text
username: editor
password: ChangeMe123!
```

## Main Routes

- `/` home
- `/about/`
- `/services/`
- `/products/`
- `/blog/`
- `/contact/`
- `/faqs/`
- `/rss/`
- `/sitemap.xml`
- `/admin/`

## Newsletter Behavior

Visitors can subscribe from the footer on every page. Subscribers are stored in the `Subscriber` model. When a blog post is saved as published and its publish date is not in the future, active subscribers receive an email containing the post title, summary, featured image, and read-more link.

Development uses Django's console email backend by default. For production, set environment variables for SMTP, SendGrid SMTP, Mailgun SMTP, Amazon SES SMTP, or another provider:

```powershell
$env:DJANGO_EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
$env:EMAIL_HOST="smtp.example.com"
$env:EMAIL_PORT="587"
$env:EMAIL_USE_TLS="1"
$env:EMAIL_HOST_USER="apikey-or-user"
$env:EMAIL_HOST_PASSWORD="secret"
$env:DEFAULT_FROM_EMAIL="news@example.com"
$env:CONTACT_TO_EMAIL="hello@example.com"
$env:SITE_URL="https://example.com"
```

## Database Configuration

**Local Development:** Uses SQLite by default (no server needed).

**Docker/Production:** Uses PostgreSQL. Set environment variables in `.env`:
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_DB`
- `POSTGRES_HOST`
- `POSTGRES_PORT`

The app automatically detects `POSTGRES_HOST` and switches from SQLite to PostgreSQL.

## Production Notes

For production deployment to Railway, Render, DigitalOcean, or AWS:
1. Set `DJANGO_SECRET_KEY` to a strong random value
2. Set `DJANGO_DEBUG=0`
3. Provide `DJANGO_ALLOWED_HOSTS` (comma-separated domains)
4. Set `POSTGRES_HOST`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`
5. Collect static files: `python manage.py collectstatic`
6. Run behind Gunicorn/Nginx or use a managed host

**GitHub Actions:** Pushes Docker image to GitHub Container Registry on every commit. Deploy the image from `ghcr.io/acewas/WWT:master`.
