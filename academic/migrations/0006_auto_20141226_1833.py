# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0005_auto_20141226_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='number',
            field=models.SmallIntegerField(default=0, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='paper',
            name='volume',
            field=models.SmallIntegerField(default=0, blank=True),
            preserve_default=False,
        ),
    ]
