# Generated by Django 4.2 on 2024-09-16 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProject', '0004_remove_blog_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artista',
            name='imagen',
        ),
        migrations.AddField(
            model_name='blog',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/'),
        ),
    ]