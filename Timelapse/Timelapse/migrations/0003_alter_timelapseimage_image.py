# Generated by Django 4.0.5 on 2022-06-25 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Timelapse', '0002_remove_timelapseimage_imagename_timelapseimage_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timelapseimage',
            name='image',
            field=models.ImageField(upload_to='Timelapse/Images'),
        ),
    ]
