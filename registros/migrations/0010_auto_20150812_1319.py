# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registros', '0009_auto_20150812_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilCliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pais', models.CharField(max_length=100, null=True, blank=True)),
                ('ciudad', models.CharField(max_length=50, null=True, blank=True)),
                ('direccion', models.CharField(max_length=50, null=True, blank=True)),
                ('telefono', models.CharField(max_length=50, null=True, blank=True)),
                ('usuario', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='perfil_cliente',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Perfil_Cliente',
        ),
    ]
