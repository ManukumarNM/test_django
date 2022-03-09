# Generated by Django 3.1.2 on 2020-11-18 12:57
# TODO: The ``replaces`` attribute needs to be removed in 0.2 release as explained in django
# docs https://docs.djangoproject.com/en/dev/topics/migrations/#migration-squashing

import uuid

import django.db.migrations.operations.special
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import swapper
from django.db import migrations, models
from django.utils.translation import gettext_lazy as _

from .. import settings as app_settings
from ..models import DeviceMonitoring


def create_device_monitoring(apps, schema_editor):
    """
    Data migration
    """
    Device = apps.get_model('config', 'Device')
    DeviceMonitoring = apps.get_model('device_monitoring', 'DeviceMonitoring')
    for device in Device.objects.all():
        DeviceMonitoring.objects.create(device=device)


class Migration(migrations.Migration):

    replaces = [
        ('device_monitoring', '0001_initial'),
        ('device_monitoring', '0002_devicemonitoring'),
    ]

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        swapper.dependency('config', 'Device', '0004_add_device_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceData',
            fields=[],
            options={
                'indexes': [],
                'proxy': True,
                'swappable': swapper.swappable_setting(
                    'device_monitoring', 'DeviceData'
                ),
            },
            bases=(swapper.get_model_name('config', 'Device'),),
        ),
        migrations.CreateModel(
            name='DeviceMonitoring',
            fields=[
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'created',
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='created',
                    ),
                ),
                (
                    'modified',
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='modified',
                    ),
                ),
                (
                    'status',
                    model_utils.fields.StatusField(
                        choices=[
                            (
                                'unknown',
                                _(app_settings.HEALTH_STATUS_LABELS['unknown']),
                            ),
                            ('ok', _(app_settings.HEALTH_STATUS_LABELS['ok'])),
                            (
                                'problem',
                                _(app_settings.HEALTH_STATUS_LABELS['problem']),
                            ),
                            (
                                'critical',
                                _(app_settings.HEALTH_STATUS_LABELS['critical']),
                            ),
                        ],
                        default='unknown',
                        db_index=True,
                        help_text=DeviceMonitoring._meta.get_field('status').help_text,
                        max_length=100,
                        no_check_for_status=True,
                        verbose_name='health status',
                    ),
                ),
                (
                    'device',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='monitoring',
                        to=swapper.get_model_name('config', 'Device'),
                    ),
                ),
            ],
            options={
                'abstract': False,
                'swappable': swapper.swappable_setting(
                    'device_monitoring', 'DeviceMonitoring'
                ),
            },
        ),
        migrations.RunPython(
            code=create_device_monitoring, reverse_code=migrations.RunPython.noop
        ),
    ]
