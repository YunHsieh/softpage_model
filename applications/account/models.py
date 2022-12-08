from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['username']

    class Meta(AbstractUser.Meta):
        db_table = 'auth'


class OutstandingToken(models.Model):
    id = models.BigAutoField(
        primary_key=True, 
        serialize=False,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
    )

    jti = models.CharField(
        unique=True, 
        max_length=255,
    )
    token = models.TextField()

    created_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField()

    class Meta:
        db_table = 'account_jwt_token'
        ordering = ('user',)

    def __str__(self):
        return "Token for {} ({})".format(
            self.user,
            self.jti,
        )


class BlacklistedToken(models.Model):
    id = models.BigAutoField(primary_key=True, serialize=False)
    token = models.OneToOneField(OutstandingToken, on_delete=models.CASCADE)
    blacklisted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'account_black_list_token'

    def __str__(self):
        return f"Blacklisted token for {self.token.user}"


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
