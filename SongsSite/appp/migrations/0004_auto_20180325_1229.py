# Generated by Django 2.0.2 on 2018-03-25 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appp', '0003_auto_20180323_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='genre',
            new_name='Song_genre',
        ),
    ]
