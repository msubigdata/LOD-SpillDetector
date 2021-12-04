from django.contrib.auth.models import User
try:
    User.objects.create_superuser('test', 'test@example.com', 'test')
except Exception:
    pass