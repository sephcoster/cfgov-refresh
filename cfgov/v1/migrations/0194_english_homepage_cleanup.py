# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-12-11 15:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0193_homepage_infounit_ordering'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepageexcludedupdates',
            name='excluded_page',
        ),
        migrations.RemoveField(
            model_name='homepageexcludedupdates',
            name='page',
        ),
        migrations.DeleteModel(
            name='HomePageExcludedUpdates',
        ),
    ]