FROM python:3.12-slim

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Show logs immediately
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]