# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20150725_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
