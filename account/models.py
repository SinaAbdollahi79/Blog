from django.db import models

# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from .managers import my_user

# class my_user(AbstractBaseUser, PermissionsMixin):
#     first_name = models.CharField(max_length=100, null=False)
#     last_name = models.CharField(max_length=100, null=False)
#     email = models.EmailField(max_length=100, null=False, unique=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     update_time = models.DateTimeField(auto_now=True, null=True, blank=True)
#     username = None
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     objects = my_user()
