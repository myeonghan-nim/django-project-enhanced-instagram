# README

## Social login

```bash
$ pip install django-allauth
```

```python
# settings.py
INSTALLED_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.kakao',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

# urls.py
urlpatterns = [
    path('auth/', include('allauth.urls')),
]
```

## Update session

```python
from django.contrib.auth import update_session_auth_hash
```

## Search with ORM

```python
from django.db.models import Q
```
