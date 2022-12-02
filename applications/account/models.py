from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['username']

    class Meta(AbstractUser.Meta):
        db_table = "auth"


# class Authemail_verification(models.Model):
#     code = models.CharField(
#         max_length=64,
#         db_index=True,
#     )
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL, 
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         db_index=True,
#     )
#     labels = models.CharField(
#         max_length=50,
#         null=True,
#         blank=True,
#         db_index=True,
#     )
#     is_published = models.BooleanField(
#         default=True,
#     )
#     create_time = models.DateTimeField(
#         auto_now_add=True,
#     )
#     update_time = models.DateTimeField(
#         auto_now=True,
#     )

#     class Meta:
#         indexes = [
#             models.Index(fields=['create_time']),
#             models.Index(fields=['update_time']),
#         ]
#         db_table = 'authemail_verification'
