# Generated by Django 3.0.1 on 2020-08-13 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(upload_to='blog-img', verbose_name='img'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]