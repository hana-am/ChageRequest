# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requst',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),

            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.AddField(
            model_name='requst',
            name='creator_id',
            field=models.ForeignKey(to='app.User'),
            preserve_default=True,
        ),
    ]
