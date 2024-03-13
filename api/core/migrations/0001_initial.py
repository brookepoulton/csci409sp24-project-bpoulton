# Generated by Django 5.0.3 on 2024-03-13 19:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillOfLading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bol_number', models.CharField(max_length=200)),
                ('contact_name', models.CharField(max_length=200)),
                ('contact_number', models.CharField(max_length=200)),
                ('contact_email', models.EmailField(max_length=200)),
                ('release_status', models.CharField(choices=[('C', 'Customs Hold'), ('S', 'Steamship Hold'), ('R', 'Released'), ('A', 'Available for Pickup')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Vessel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vessel_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('container_number', models.CharField(max_length=200)),
                ('bol', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.billoflading')),
            ],
        ),
        migrations.CreateModel(
            name='VesselSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voyage_number', models.CharField(max_length=50)),
                ('arrival_date', models.DateField()),
                ('vessel', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.vessel')),
            ],
        ),
        migrations.AddField(
            model_name='billoflading',
            name='voyage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.vesselschedule'),
        ),
    ]
