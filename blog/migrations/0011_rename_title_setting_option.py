# Generated by Django 4.0 on 2021-12-27 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_rename_option_setting_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='title',
            new_name='option',
        ),
    ]