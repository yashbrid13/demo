# Generated by Django 4.1.7 on 2023-03-24 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_articlemedia_url_articlerating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='domain',
            old_name='isisactive',
            new_name='isactive',
        ),
    ]