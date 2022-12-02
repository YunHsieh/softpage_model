import uuid

from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField


class Softessay_Topic(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False,
    )
    name = models.CharField(
        max_length=256,
        db_index=True,
    )
    create_time = models.DateTimeField(
        auto_now_add=True,
    )
    update_time = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        indexes = [
            # this is Django 4.0 newest useage
            models.Index(fields=['name']),
            models.Index(fields=['create_time']),
            models.Index(fields=['update_time']),
        ]
        db_table = 'softessay_topic'


class Softessay_Tag(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False,
    )
    name = models.CharField(
        max_length=256,
        db_index=True,
    )
    create_time = models.DateTimeField(
        auto_now_add=True,
    )
    update_time = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['create_time']),
            models.Index(fields=['update_time']),
        ]
        db_table = 'softessay_tag'


class Softessay_Essay(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False,
    )
    title = models.ForeignKey(
        Softessay_Topic, 
        on_delete=models.PROTECT,
    )
    version = models.CharField(
        max_length=32,
    )
    content = models.TextField()
    is_published = models.BooleanField(
        max_length=256,
    )
    is_deleted = models.BooleanField(
        max_length=256,
        default=False,
    )
    sequence = ArrayField(
        models.CharField(
            max_length=32,
        ),
        size=128,
    )
    tag = models.ForeignKey(
        Softessay_Tag, 
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    forker = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT,
        related_name='forker',
        null=True,
        blank=True,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT,
        related_name='author',
        null=True,
        blank=True,
    )
    create_time = models.DateTimeField(
        auto_now_add=True,
    )
    update_time = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        indexes = [
            models.Index(fields=['create_time']),
            models.Index(fields=['update_time']),
        ]
        db_table = 'softessay_essay'


class Softessay_Body(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False,
    )
    parent_body = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    content = models.TextField()
    essay = models.ForeignKey(
        Softessay_Essay, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    create_time = models.DateTimeField(
        auto_now_add=True,
    )
    update_time = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        indexes = [
            models.Index(fields=['create_time']),
            models.Index(fields=['update_time']),
        ]
        db_table = 'softessay_body'


class Softessay_Comment(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False,
    )
    parent_body = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    comment = models.TextField()
    essay = models.ForeignKey(
        Softessay_Essay, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    create_time = models.DateTimeField(
        auto_now_add=True,
    )
    update_time = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        indexes = [
            models.Index(fields=['create_time']),
            models.Index(fields=['update_time']),
        ]
        db_table = 'softessay_comment'
