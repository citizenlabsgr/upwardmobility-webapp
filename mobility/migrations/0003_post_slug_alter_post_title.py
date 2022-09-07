# Generated by Django 4.0.6 on 2022-08-01 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobility', '0002_alter_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='asdf', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
