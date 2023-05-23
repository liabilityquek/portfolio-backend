# Generated by Django 4.2.1 on 2023-05-18 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('greeting', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('par_inro', models.TextField(blank=True, null=True)),
                ('avatar_img', models.ImageField(blank=True, max_length=60, null=True, upload_to='./images')),
                ('cv_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
