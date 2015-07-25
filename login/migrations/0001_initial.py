# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('username', models.CharField(unique=True, max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phoneNo', models.BigIntegerField()),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('fathersName', models.CharField(max_length=50)),
                ('DOB', models.DateField()),
                ('isCR', models.BooleanField()),
                ('studentID', models.CharField(max_length=50)),
                ('batchID', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=30)),
                ('admissionYear', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('url', models.URLField(unique=True, max_length=50)),
                ('batchID', models.CharField(max_length=50)),
                ('dueDate', models.DateField()),
                ('teacherID', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('batchID', models.CharField(unique=True, max_length=50)),
                ('year', models.CharField(max_length=5)),
                ('studentCount', models.BigIntegerField()),
                ('subjectCount', models.BigIntegerField()),
                ('cr', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('username', models.CharField(unique=True, max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=20)),
                ('roomNo', models.CharField(max_length=10)),
                ('designation', models.CharField(max_length=20)),
                ('expertise', models.CharField(max_length=20)),
                ('phoneNo', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('dateOfJoining', models.DateField()),
                ('isHOD', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('batchID', models.CharField(unique=True, max_length=50)),
                ('teacherID', models.CharField(max_length=30)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('day', models.CharField(max_length=10)),
                ('subjectID', models.CharField(max_length=30)),
                ('venue', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
