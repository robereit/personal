# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0007_auto_20141226_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='page_nums',
            field=models.CharField(max_length=25, blank=True),
            preserve_default=True,
        ),
    ]
