# Generated by Django 4.2.1 on 2023-05-26 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_remove_socialmedialinks_social_icon'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.RemoveField(
            model_name='socialmedialinks',
            name='link_created_at',
        ),
        migrations.RemoveField(
            model_name='socialmedialinks',
            name='link_updated_at',
        ),
        migrations.AlterField(
            model_name='socialmedialinks',
            name='link',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
