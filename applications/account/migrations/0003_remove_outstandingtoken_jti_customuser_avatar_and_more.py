# Generated by Django 4.1.3 on 2023-01-02 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_outstandingtoken_blacklistedtoken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outstandingtoken',
            name='jti',
        ),
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='outstandingtoken',
            name='issuer',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
