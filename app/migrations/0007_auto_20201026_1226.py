# Generated by Django 3.1.2 on 2020-10-26 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201026_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='airport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.airport'),
        ),
    ]
