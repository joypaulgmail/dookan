# Generated by Django 3.1 on 2021-02-08 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reglog', '0022_auto_20210208_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewproduct',
            name='star',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]