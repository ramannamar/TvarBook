# Generated by Django 5.0.1 on 2024-01-07 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_usernet_bio_usernet_birth_date_usernet_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernet',
            name='middle_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usernet',
            name='phone_number',
            field=models.CharField(max_length=14, null=True),
        ),
    ]