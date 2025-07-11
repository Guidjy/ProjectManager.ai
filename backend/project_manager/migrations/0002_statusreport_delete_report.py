# Generated by Django 5.2.3 on 2025-06-27 00:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=2500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('document', models.FileField(upload_to='documents/status_reports/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_reports', to='project_manager.project')),
            ],
        ),
        migrations.DeleteModel(
            name='Report',
        ),
    ]
