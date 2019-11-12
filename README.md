# Really faked Instagram

### Social login

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
    path('accounts/', include('allauth.urls')),
]
```

### Update session

```python
from django.contrib.auth import update_session_auth_hash
```

### Search with Django ORM

```python
from django.db.models import Q
```
