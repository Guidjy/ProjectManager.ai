# Generated by Django 5.2.3 on 2025-06-27 01:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0004_alter_project_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statusreport',
            name='content',
        ),
        migrations.CreateModel(
            name='CurrentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=5000)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_status', to='project_manager.project')),
            ],
        ),
    ]
