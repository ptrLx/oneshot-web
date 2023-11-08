# --- nginx --- #

FROM nginx:latest AS builder

COPY deploy/nginx.conf /etc/nginx/nginx.conf

# --- supervisor --- #

RUN apt-get update && apt-get install -y supervisor

COPY deploy/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# --- api --- #

FROM python:3.11

RUN pip install pipenv

COPY backend/api /api

WORKDIR /api

RUN pipenv install --deploy

# --- frontend --- #

COPY frontend/dist /var/www/html

# --- start --- #

EXPOSE 80
CMD ["/usr/bin/supervisord"]
