# Deployment of oneshot-web

Attention: oneshot-web comes with absolutely no warranty and is currently in beta phase! Please check out the repository on [GitHub](https://github.com/ptrLx/oneshot-web).

Use following `docker-compose.yml`-template to host oneshot-web:

```yml
version: '3.9'

services:
  db:
    container_name: oneshot-web-db
    image: 'postgres:latest'
    env_file:
      - .env
    networks:
      - oneshot-web-db
    volumes:
      - ./db/:/var/lib/postgresql/data/:Z
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql:ro
    restart: unless-stopped

  app:
    image: ptrlx/oneshot-web:latest
    container_name: oneshot-web-app
    ports:
      - 8080:80
    env_file:
      - .env
    networks:
      - oneshot-web-db
    depends_on:
      db:
        condition: service_started
    volumes:
      - ./app/:/srv/oneshot:Z
    restart: unless-stopped

networks:
  oneshot-web-db:
    driver: bridge
```

Store the `.env` file and the `ìnit.sql` file next to the `docker-compose.yml`

`.env`:

```conf
DATABASE_HOST="oneshot-web-db"
HOST_URL="change-host-url.example.com"
POSTGRES_PASSWORD="change_this_password"
TZ="Europe/Berlin"
```

`init.sql`:

```sql
CREATE DATABASE osweb;
GRANT ALL PRIVILEGES ON DATABASE osweb TO postgres;
```

## Start the admintools to create a user

```bash
docker exec -it oneshot-web-app /bin/bash -c "cd /api && pipenv run python admintools/main.py"
```
