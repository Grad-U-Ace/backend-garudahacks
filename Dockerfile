FROM python:3.12-slim

ENV APP_HOME /app
WORKDIR $APP_HOME

# Removes output stream buffering, allowing for more efficient logging
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy local code to the container image.
COPY . .

CMD exec gunicorn --bind :8000 --workers 1 --threads 8 --timeout 0 guruda_api.wsgi:application