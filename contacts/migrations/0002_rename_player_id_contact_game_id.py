# Generated by Django 4.1.7 on 2023-05-25 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='player_id',
            new_name='game_id',
        ),
    ]