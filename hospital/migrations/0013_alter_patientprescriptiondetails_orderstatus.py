# Generated by Django 3.2.9 on 2022-01-15 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0012_auto_20220115_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientprescriptiondetails',
            name='orderStatus',
            field=models.CharField(max_length=100),
        ),
    ]