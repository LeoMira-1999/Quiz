# Generated by Django 3.2.5 on 2021-11-01 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0011_alter_score_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]
