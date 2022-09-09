# Generated by Django 4.1.1 on 2022-09-08 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coachescornerapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='college',
            old_name='location',
            new_name='city',
        ),
        migrations.AddField(
            model_name='college',
            name='state',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
