# Codex Commerce Django Website

A commercial Django website with business pages, services, products, pricing, testimonials, searchable blog, comments, newsletter subscriptions, contact messages, RSS, sitemap, and Django admin management.

## Quick Start

```powershell
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

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

## Production Notes

Use PostgreSQL for production, configure `DJANGO_SECRET_KEY`, set `DJANGO_DEBUG=0`, provide `DJANGO_ALLOWED_HOSTS`, collect static files, and run behind Gunicorn/Nginx or a managed host like Render, Railway, PythonAnywhere, DigitalOcean, or AWS.
