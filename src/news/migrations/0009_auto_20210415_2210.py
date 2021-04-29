# Generated by Django 3.1.7 on 2021-04-15 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0008_auto_20210415_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='view_count',
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail_alt',
            field=models.ImageField(upload_to=''),
        ),
        migrations.CreateModel(
            name='PostView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
