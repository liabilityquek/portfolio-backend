# Generated by Django 4.2.1 on 2023-05-26 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0005_portfolio_project_demo_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='project_updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
