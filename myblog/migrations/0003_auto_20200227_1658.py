# Generated by Django 2.2.7 on 2020-02-27 14:58

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='comment',
            managers=[
                ('active_comments', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]
