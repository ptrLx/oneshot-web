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

### /user

> GET

attribute:

* token

response:

```json
{
    "profilepic": "url",
    "username": "username",
    "full-name": "name",
    // "role": "role"
}
```

### /user/profilepic

> POST

attribute:

* token

<!-- upload file -->

response:

```json
{
    "ok"
}
```

### /user/password

> POST

attribute:

* token

parameter:

* oldpw
* newpw

response:

```json
{
    "ok"
}
```

### /user/logout

> POST

attribute:

* token

response:

```json
{
    "ok"
}
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

* date
* time
* happiness?
* text?

response:

```json
{
    "ok"
}
```

### /image/update

> POST

attribute:

* token

parameter:

* date
* happiness?
* text?

response:

```json
{
    "ok"
}
```

### /image/delete

> POST

attribute:

* token

parameter:

* date

response:

```json
{
    "ok"
}
```

### /image/preview

> GET

attribute:

* token

parameter:

* date

response:

<!-- image file -->

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

### calendar/preview

> GET

attribute:

* token

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
        ... x28 entries
    ]
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
