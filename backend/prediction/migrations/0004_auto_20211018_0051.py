# Generated by Django 3.2.6 on 2021-10-17 23:51

from django.db import migrations, models
import prediction.models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0003_rename_prediction_columns_trainingmodel_feature_columns'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingmodel',
            name='cleaned_dataset',
            field=models.FileField(blank=True, upload_to='models/cleaned'),
        ),
        migrations.AlterField(
            model_name='trainingmodel',
            name='dataset',
            field=models.FileField(upload_to='models', validators=[prediction.models.validate_dataset]),
        ),
        migrations.AlterField(
            model_name='trainingmodel',
            name='feature_columns',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trainingmodel',
            name='target_column',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
