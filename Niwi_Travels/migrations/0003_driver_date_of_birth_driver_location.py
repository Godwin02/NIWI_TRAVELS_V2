# Generated by Django 4.2.5 on 2023-10-27 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Niwi_Travels', '0002_alter_user_is_traveller'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
