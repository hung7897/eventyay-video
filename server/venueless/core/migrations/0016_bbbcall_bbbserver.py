# Generated by Django 3.0.6 on 2020-07-05 17:41

import uuid

import django.db.models.deletion
from django.db import migrations, models

import venueless.core.models.bbb


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0015_room_pretalx_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="BBBServer",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("active", models.BooleanField(default=True)),
                ("url", models.URLField()),
                ("secret", models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="BBBCall",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "meeting_id",
                    models.CharField(
                        default=venueless.core.models.bbb.random_key, max_length=300
                    ),
                ),
                (
                    "attendee_pw",
                    models.CharField(
                        default=venueless.core.models.bbb.random_key, max_length=300
                    ),
                ),
                (
                    "moderator_pw",
                    models.CharField(
                        default=venueless.core.models.bbb.random_key, max_length=300
                    ),
                ),
                (
                    "room",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bbb_call",
                        to="core.Room",
                    ),
                ),
                (
                    "server",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.BBBServer"
                    ),
                ),
                (
                    "world",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bbb_calls",
                        to="core.World",
                    ),
                ),
            ],
        ),
    ]