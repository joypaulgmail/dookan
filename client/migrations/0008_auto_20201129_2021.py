# Generated by Django 3.1 on 2020-11-29 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_auto_20201128_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientinformation',
            name='id',
        ),
        migrations.AlterField(
            model_name='clientinformation',
            name='email',
            field=models.EmailField(default=True, max_length=254, serialize=False),
            preserve_default=False,
        ),
    ]
