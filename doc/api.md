# API definition

### /login

> GET

parameter:

* user
* password

response:

```json
{
    "token": "ey..."
}
```

### /user/me

> GET

attribute:

* token

response:

```json
{
    "profileimg": "url",
    "username": "username",
    "full-name": "name",
    "role": "role"
}
```

### /user/profileimg

> POST

attribute:

* token

<!-- upload file -->

response:

```json
"ok"
```

> GET

attribute:

* token

response:

<!-- image file -->

### /user/chpw

> POST

attribute:

* token

parameter:

* oldpw
* newpw

response:

```json
"ok"
```

### /user/preferences

### /db/import

### /db/export

### /image/upload

> POST

attribute:

* token

<!-- upload file -->

parameter:

* oneshot-update (see api-types.md)

response:

```json
"ok"
```

### /image/update

> POST

attribute:

* token

parameter:

* oneshot (see api-types.md)

response:

```json
"ok"
```

### /image/delete

> POST

attribute:

* token

parameter:

* date

response:

```json
"ok"
```

### /image/gallery

> GET

attribute:

* token

parameter:

* page: number
* size: number

response:

```json
{
    [
        {
            "date": "date",
            "image": "url",
            "happiness": "happiness"
        },
        {
            "date": "date",
            "image": "url",
            "happiness": "happiness"

        },
        {
            "date": "date",
            "image": "url",
            "happiness": "happiness"

        },
        {
            "date": "date",
            "image": "url",
            "happiness": "happiness"

        },
    ]
    ...
}
```

### flashback

> GET

attribute:

* token

response:

```json
{
    "random_happy": {
        "date": "date",
        "image": "url",
        "happiness": "HAPPINESS"
    },
    "last_very_happy_day": {
        "date": "date",
        "image": "url",
        "happiness": "HAPPINESS"
    },
    // "yesterday": {
    //    "date": "date",
    //     "image": "url",
    //     "happiness": "HAPPINESS"
    // },
    "same_date_last_month": {
        "date": "date",
        "image": "url",
        "happiness": "HAPPINESS"
    },
    "same_date_last_years": [
        {
            "date": "date",
            "image": "url",
            "happiness": "HAPPINESS"
        },
        {
            "date": "date",
            "image": "url",
            "happiness": "HAPPINESS"
        }
    ],
    ...
}
```

### calendar

> GET

attribute:

* token

parameter:

* month

response:

```json
{
    [
        {
            "date": "date",
            "happiness_state": "HAPPINESS",
        },
        {
            "date": "date",
            "happiness_state": "NO_ENTRY",
        },
        ...
    ]
}
```

### stat
