# Generated by Django 4.1.7 on 2023-03-24 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_active_article_isactive_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='source',
        ),
        migrations.RemoveField(
            model_name='historicalarticle',
            name='source',
        ),
        migrations.DeleteModel(
            name='Source',
        ),
    ]
