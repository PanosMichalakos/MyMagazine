# Generated by Django 3.1.7 on 2021-04-08 08:10

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_remove_post_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='next_post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='previous_post',
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default=''),
        ),
    ]
