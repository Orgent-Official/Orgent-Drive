# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drives', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('link', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Files',
            },
        ),
        migrations.RenameField(
            model_name='folder',
            old_name='text',
            new_name='name',
        ),
        migrations.AddField(
            model_name='file',
            name='Folder',
            field=models.ForeignKey(to='drives.Folder'),
        ),
    ]
