# Generated by Django 4.1.1 on 2022-09-15 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coachescornerapi', '0006_remove_player_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='position',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='profilepics'),
        ),
    ]