# Generated by Django 2.2.1 on 2019-05-29 04:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
