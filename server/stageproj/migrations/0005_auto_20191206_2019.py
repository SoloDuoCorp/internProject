# Generated by Django 3.0 on 2019-12-06 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stageproj', '0004_charset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='editorUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stageproj.User'),
        ),
    ]
