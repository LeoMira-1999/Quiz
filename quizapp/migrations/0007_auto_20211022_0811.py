# Generated by Django 3.2.5 on 2021-10-22 08:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizapp', '0006_auto_20211015_1226'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Result',
            new_name='Score',
        ),
        migrations.RemoveField(
            model_name='images',
            name='created',
        ),
        migrations.RemoveField(
            model_name='question',
            name='created',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='required_score_to_pass',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='time',
        ),
        migrations.AddField(
            model_name='images',
            name='cell_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='images',
            name='component',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='images',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='images',
            name='doi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='images',
            name='microscopy',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='images',
            name='organism',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='points',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
    ]
