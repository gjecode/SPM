# Generated by Django 4.1.1 on 2022-10-28 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LJPS', '0002_job_role_job_role_status_skill_skill_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='Role_ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='staff',
            name='Staff_ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]