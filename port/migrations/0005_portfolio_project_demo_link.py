# Generated by Django 4.2.1 on 2023-05-19 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0004_alter_portfolio_project_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='project_demo_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]