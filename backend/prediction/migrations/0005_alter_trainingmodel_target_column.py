# Generated by Django 3.2.6 on 2021-10-18 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0004_auto_20211018_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingmodel',
            name='target_column',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
