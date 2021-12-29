# Generated by Django 4.0 on 2021-12-27 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_setting_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='option',
            field=models.CharField(choices=[('blog_title', 'Blog Title'), ('blog_about', 'Blog About'), ('blog_social_media', 'Blog Social Media')], max_length=32, unique=True),
        ),
    ]