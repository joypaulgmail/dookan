# Generated by Django 3.1 on 2020-12-14 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0010_remove_clientinformation_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientinformation',
            name='idproof',
            field=models.ImageField(blank=True, upload_to='client/id'),
        ),
    ]