# Generated by Django 4.2.6 on 2023-10-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='job_Art',
        ),
        migrations.AddField(
            model_name='job',
            name='job_natur',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Remote', 'Remote'), ('Freelance', 'Freelance')], default=0, max_length=100),
            preserve_default=False,
        ),
    ]
