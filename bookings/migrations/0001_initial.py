# Generated by Django 4.1.3 on 2023-04-04 03:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('logo', models.ImageField(default='sample_user.png', upload_to='logos', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])])),
                ('wifi', models.BooleanField()),
                ('pickup', models.BooleanField()),
                ('water', models.BooleanField()),
                ('allService', models.BooleanField()),
                ('telephone', models.BooleanField()),
            ],
        ),
    ]
