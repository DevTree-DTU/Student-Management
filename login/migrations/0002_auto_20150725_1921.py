# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='DOB',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='admissionYear',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='batchID',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='fathersName',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='isCR',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentID',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
