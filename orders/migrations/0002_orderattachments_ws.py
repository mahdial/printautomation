# Generated by Django 3.0 on 2019-12-29 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderattachments',
            name='ws',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='orders.WorkStations'),
        ),
    ]
