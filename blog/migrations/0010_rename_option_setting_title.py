# Generated by Django 4.0 on 2021-12-27 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_setting_option'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='option',
            new_name='title',
        ),
    ]
