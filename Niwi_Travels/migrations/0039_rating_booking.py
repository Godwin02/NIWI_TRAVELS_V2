# Generated by Django 4.2.5 on 2024-03-17 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Niwi_Travels', '0038_passenger_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='booking',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='Niwi_Travels.booking'),
        ),
    ]
