# Generated by Django 4.2.5 on 2023-11-04 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Niwi_Travels', '0008_remove_travelpackage_meals_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger_name', models.CharField(max_length=100)),
                ('passenger_age', models.PositiveIntegerField()),
                ('proof_of_id', models.FileField(upload_to='passenger_ids/')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Niwi_Travels.travelpackage')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]