FROM python:3.11-bullseye

# --- general --- #

RUN apt-get update && apt-get install -y supervisor nginx && rm -rf /var/lib/apt/lists/*
RUN pip install pipenv

# --- api --- #

WORKDIR /api

# Install dependencies first to save build time on rebuilds.
COPY backend/api/Pipfile* /api
RUN pipenv install --deploy

# Build prisma client from schema.prisma file
COPY backend/api/prisma /api/prisma
RUN pipenv run prisma generate

# Add alias for admintools
RUN echo 'alias admintools="cd /api && pipenv run python admintools/main.py"' >> ~/.bashrc

# Copy source code of api and admintools
COPY backend/api/src /api/src
COPY backend/api/admintools /api/admintools

# --- nginx --- #

COPY container-assets/nginx.conf /etc/nginx/nginx.conf

# --- supervisor --- #

COPY container-assets/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# --- frontend --- #

COPY frontend/dist /var/www/html

# --- start --- #

EXPOSE 80
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
