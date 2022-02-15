# Generated by Django 4.0 on 2022-01-17 17:48

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('webapp', '0007_postmodel_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='author',
            field=models.ForeignKey(default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='auth.user'),
        ),
    ]