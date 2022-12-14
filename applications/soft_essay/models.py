import uuid

from django.db import models
from django.db.models import JSONField
from django.conf import settings


class Softessay_Topic(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False,
    )
    name = models.CharField(
        max_length=256,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='topic unique name')
        ]
        indexes = [
            # this is Django 4.0 newest useage
            models.Index(fields=['name']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at']),
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
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='tag unique name')
        ]
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at']),
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
        null=True,
        blank=True,
    )
    content = models.TextField()
    is_published = models.BooleanField(
        default=True,
    )
    is_deleted = models.BooleanField(
        default=False,
    )
    order_seq = JSONField()
    tag = models.ManyToManyField(
        Softessay_Tag, 
        through='EssayTag',
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
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author', 'forker'], 
                name='unique essay by author'
            )
        ]
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at']),
        ]
        db_table = 'softessay_essay'


class EssayTag(models.Model):
    id = models.AutoField(primary_key=True)
    essay = models.ForeignKey(Softessay_Essay, on_delete=models.CASCADE)
    tag = models.ForeignKey(Softessay_Tag, on_delete=models.CASCADE)
        
    class Meta:
        db_table = 'essay_x_tag'


class Softessay_Body(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False,
    )
    last_version = models.ForeignKey(
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
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at']),
        ]
        db_table = 'softessay_body'


class Softessay_Comment(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False,
    )
    last_comment = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    comment = models.TextField()
    body = models.ForeignKey(
        Softessay_Body, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    essay = models.ForeignKey(
        Softessay_Essay, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at']),
        ]
        db_table = 'softessay_comment'
