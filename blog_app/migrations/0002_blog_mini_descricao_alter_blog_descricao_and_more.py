# Generated by Django 4.1.4 on 2022-12-10 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='mini_descricao',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='descricao',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='blog',
            name='titulo',
            field=models.CharField(max_length=1000),
        ),
    ]
