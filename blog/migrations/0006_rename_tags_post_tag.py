# Generated by Django 4.0 on 2021-12-27 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_posted_date_post_published_date_post_tags_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tags',
            new_name='tag',
        ),
    ]
