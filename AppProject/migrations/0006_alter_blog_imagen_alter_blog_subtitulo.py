# Generated by Django 4.2 on 2024-09-16 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProject', '0005_remove_artista_imagen_blog_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='blogs/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='subtitulo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
