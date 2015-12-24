# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_requst_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='requst',
            name='status',
            field=models.CharField(default=0, max_length=10, choices=[(b'1', b'approved'), (b'0', b'unapproved')]),
            preserve_default=False,
        ),
    ]
