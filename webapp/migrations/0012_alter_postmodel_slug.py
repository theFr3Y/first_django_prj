# Generated by Django 4.0 on 2022-02-15 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='slug',
            field=models.SlugField(default='uwdilthjfm', max_length=200, unique=True),
        ),
    ]
