# Generated by Django 5.0.1 on 2024-01-07 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_usernet_middle_name_alter_usernet_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernet',
            name='middle_name',
            field=models.CharField(max_length=50),
        ),
    ]