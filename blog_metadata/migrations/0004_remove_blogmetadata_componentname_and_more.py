# Generated by Django 5.0.4 on 2024-06-23 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_metadata', '0003_alter_blogmetadata_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmetadata',
            name='componentName',
        ),
        migrations.AddField(
            model_name='blogmetadata',
            name='content',
            field=models.TextField(null=True),
        ),
    ]