# How to use the api

## Start the api

* `make start-api`
* visit <http://localhost:8200/docs>

## Request access token

> provide username and password.

```bash
curl -X 'POST' \
  'http://localhost:8200/login/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=&username=john&password=password&scope=&client_id=&client_secret='
```

response:

```json
{"access_token":"ey...","token_type":"bearer"}
```

## Send api requests

> provide your token

```bash
curl -X 'GET' \
  'http://localhost:8200/user/me' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer ey...'
```

response:

```json
{"username":"john","role":"admin","disabled":false,"full_name":"John Doe","profileimg":null}
```
