# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='length',
            field=models.CharField(max_length=25),
            preserve_default=True,
        ),
    ]
