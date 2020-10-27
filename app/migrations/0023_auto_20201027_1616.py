# Generated by Django 3.1.2 on 2020-10-27 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20201027_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activepilot',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.club'),
        ),
        migrations.AlterField(
            model_name='activepilot',
            name='pilot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pilot'),
        ),
    ]
