# Generated by Django 3.2.8 on 2022-03-20 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0002_auto_20220320_0913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='nome',
            new_name='nome_animal',
        ),
    ]
