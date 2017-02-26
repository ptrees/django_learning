# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 04:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='\u6807\u9898')),
                ('auther', models.CharField(max_length=64, verbose_name='\u4f5c\u8005')),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u8868\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
            ],
        ),
    ]
