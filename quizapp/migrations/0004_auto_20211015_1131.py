# Generated by Django 3.2.5 on 2021-10-15 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0003_alter_images_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='image',
        ),
        migrations.AddField(
            model_name='images',
            name='image_path',
            field=models.CharField(default='static/images/187.png', max_length=200),
        ),
    ]
