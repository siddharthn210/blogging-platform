# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 05:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=128, unique=True)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PostComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_type', models.IntegerField(choices=[(1, 'Paragraph')])),
                ('text', models.TextField()),
                ('order_rank', models.IntegerField(default=1)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogentries.Post')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post_component',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogentries.PostComponent'),
        ),
    ]
