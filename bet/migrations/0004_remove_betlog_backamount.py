# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-10 11:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0003_paymentbacklog_fee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='betlog',
            name='backAmount',
        ),
    ]
