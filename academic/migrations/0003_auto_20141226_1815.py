# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0002_auto_20141226_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_code',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
