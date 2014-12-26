# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0003_auto_20141226_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseinstance',
            name='year',
        ),
        migrations.AddField(
            model_name='courseinstance',
            name='semester',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
