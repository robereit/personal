# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0004_auto_20141226_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='number',
            field=models.SmallIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='paper',
            name='volume',
            field=models.SmallIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='paper',
            name='year',
            field=models.CharField(max_length=4),
            preserve_default=True,
        ),
    ]
