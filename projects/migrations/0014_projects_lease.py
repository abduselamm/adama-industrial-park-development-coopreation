# Generated by Django 4.1 on 2022-09-11 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_rename_project_projects_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='lease',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.lease'),
        ),
    ]
