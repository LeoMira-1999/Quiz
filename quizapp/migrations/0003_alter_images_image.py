# Generated by Django 3.2.5 on 2021-10-15 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0002_auto_20211015_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
