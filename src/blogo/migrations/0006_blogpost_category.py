# Generated by Django 3.1.6 on 2023-03-16 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogo', '0005_blogpost_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ManyToManyField(to='blogo.Category'),
        ),
    ]
