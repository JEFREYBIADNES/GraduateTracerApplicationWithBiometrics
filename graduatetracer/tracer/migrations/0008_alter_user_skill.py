# Generated by Django 4.0.5 on 2023-01-24 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracer', '0007_alter_advertise_job_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='skill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tracer.jobcategory'),
        ),
    ]
