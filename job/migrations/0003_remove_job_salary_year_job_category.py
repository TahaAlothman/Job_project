# Generated by Django 4.2.6 on 2023-10-16 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_remove_job_job_art_job_job_natur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='salary_year',
        ),
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='job_category', to='job.category'),
            preserve_default=False,
        ),
    ]