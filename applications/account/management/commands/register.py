from django.core.management.base import BaseCommand, CommandError
from applications.account.models import CustomUser
from django.conf import settings
from passlib.hash import pbkdf2_sha256


def make_password(password):
    return pbkdf2_sha256.hash(f'{password}{settings.SECRET_KEY}')


class Command(BaseCommand):
    help = 'Create the new fake account'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)

    def handle(self, *args, **options):
        username, password = options['username'], options['password']
        instance = CustomUser(
            username=username,
            email=f'{username}@example.com',
            password=make_password(password),
        )
        instance.save()
