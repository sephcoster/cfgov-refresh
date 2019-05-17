# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-15 07:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('wagtailcore', '0040_page_draft_title'),
        ('v1', '0157_create_glossary_term'),
        ('wagtailinventory', '0001_initial'),
        ('ask_cfpb', '0029_answer_schema_blocks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answercategorypage',
            name='ask_category',
        ),
        migrations.RemoveField(
            model_name='answercategorypage',
            name='ask_subcategory',
        ),
        migrations.RemoveField(
            model_name='answercategorypage',
            name='cfgovpage_ptr',
        ),
        migrations.DeleteModel(
            name='AnswerCategoryPage',
        ),
    ]