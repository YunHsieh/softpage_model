from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)
    avatar = models.TextField(null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    REQUIRED_FIELDS = ['username']

    class Meta(AbstractUser.Meta):
        db_table = 'auth'


class OutstandingToken(models.Model):
    id = models.BigAutoField(
        primary_key=True, 
        serialize=False,
    )
    issuer = models.CharField(
        max_length=512,
        null=True, 
        blank=True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
    )
    token = models.TextField()
    created_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField()

    class Meta:
        db_table = 'account_jwt_token'
        ordering = ('user',)

    def __str__(self):
        return self.user


class BlacklistedToken(models.Model):
    id = models.BigAutoField(primary_key=True, serialize=False)
    token = models.OneToOneField(OutstandingToken, on_delete=models.CASCADE)
    blacklisted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'account_black_list_token'

    def __str__(self):
        return f"Blacklisted token for {self.token.user}"


# TODO: verify the email
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
