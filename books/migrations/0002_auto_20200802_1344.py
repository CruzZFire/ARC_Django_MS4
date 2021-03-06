# Generated by Django 3.0.8 on 2020-08-02 11:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='language_code',
            field=models.CharField(default='eng', max_length=5),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_year',
            field=models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
    ]
