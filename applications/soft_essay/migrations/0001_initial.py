# Generated by Django 4.1.3 on 2022-12-02 07:30

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Softessay_Body',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'softessay_body',
            },
        ),
        migrations.CreateModel(
            name='Softessay_Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'softessay_comment',
            },
        ),
        migrations.CreateModel(
            name='Softessay_Essay',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('version', models.CharField(max_length=32)),
                ('content', models.TextField()),
                ('is_published', models.BooleanField(max_length=256)),
                ('is_deleted', models.BooleanField(default=False, max_length=256)),
                ('sequence', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32), size=128)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'softessay_essay',
            },
        ),
        migrations.CreateModel(
            name='Softessay_Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=256)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'softessay_tag',
            },
        ),
        migrations.CreateModel(
            name='Softessay_Topic',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=256)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'softessay_topic',
            },
        ),
        migrations.AddIndex(
            model_name='softessay_topic',
            index=models.Index(fields=['name'], name='softessay_t_name_4d0e44_idx'),
        ),
        migrations.AddIndex(
            model_name='softessay_topic',
            index=models.Index(fields=['create_time'], name='softessay_t_create__f3f775_idx'),
        ),
        migrations.AddIndex(
            model_name='softessay_topic',
            index=models.Index(fields=['update_time'], name='softessay_t_update__335988_idx'),
        ),
        migrations.AddIndex(
            model_name='softessay_tag',
            index=models.Index(fields=['name'], name='softessay_t_name_bb583f_idx'),
        ),
        migrations.AddIndex(
            model_name='softessay_tag',
            index=models.Index(fields=['create_time'], name='softessay_t_create__a1d42e_idx'),
        ),
        migrations.AddIndex(
            model_name='softessay_tag',
            index=models.Index(fields=['update_time'], name='softessay_t_update__801ba5_idx'),
        ),
        migrations.AddField(
            model_name='softessay_essay',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='softessay_essay',
            name='forker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='forker', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='softessay_essay',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='soft_essay.softessay_tag'),
        ),
        migrations.AddField(
            model_name='softessay_essay',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='soft_essay.softessay_topic'),
        ),
        migrations.AddField(
            model_name='softessay_comment',
            name='essay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='soft_essay.softessay_essay'),
        ),
        migrations.AddField(
            model_name='softessay_comment',
            name='parent_body',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='soft_essay.softessay_comment'),
        ),
        migrations.AddField(
            model_name='softessay_body',
            name='essay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='soft_essay.softessay_essay'),
        ),
        migrations.AddField(
            model_name='softessay_body',
            name='parent_body',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='soft_essay.softessay_body'),
        ),
        migrations.AddIndex(
            model_name='softessay_essay',
            index=models.Index(fields=['create_time'], name='softessay_e_create__b0b8c9_idx'),
        ),
        migrations.AddIndex(
            model_name='softessay_essay',
            index=models.Index(fields=['update_time'], name='softessay_e_update__49da23_idx'),
        ),
        migrations.AddIndex(
            model_name='softessay_comment',
            index=models.Index(fields=['create_time'], name='softessay_c_create__bbd060_idx'),
        ),
        migrations.AddIndex(
            model_name='softessay_comment',
            index=models.Index(fields=['update_time'], name='softessay_c_update__b59de6_idx'),
        ),
        migrations.AddIndex(
            model_name='softessay_body',
            index=models.Index(fields=['create_time'], name='softessay_b_create__f5ae0f_idx'),
        ),
        migrations.AddIndex(
            model_name='softessay_body',
            index=models.Index(fields=['update_time'], name='softessay_b_update__020eca_idx'),
        ),
    ]