# Generated by Django 4.1.7 on 2023-03-24 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_articleinteraction_delete_articlerating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='writer',
            name='isEditor',
        ),
        migrations.RemoveField(
            model_name='writer',
            name='isWriter',
        ),
        migrations.AddField(
            model_name='articleinteraction',
            name='bookmarked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='isEditor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='isWriter',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='static/icons/')),
                ('hash_tags', models.ManyToManyField(to='core.hashtag')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='static/icons/')),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
                ('domain', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.domain')),
                ('submenu', models.ManyToManyField(to='core.submenu')),
            ],
        ),
    ]