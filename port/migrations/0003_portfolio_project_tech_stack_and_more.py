# Generated by Django 4.2.1 on 2023-05-18 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0002_portfolio_project_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='project_tech_stack',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='project_description',
            field=models.CharField(max_length=1000),
        ),
    ]
