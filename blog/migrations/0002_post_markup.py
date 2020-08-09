# Generated by Django 2.2.15 on 2020-08-09 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='markup',
            field=models.SlugField(choices=[('html', 'HTML'), ('md', 'Markdown'), ('rst', 'reStructuredText'), ('txt', 'Text')], default='md'),
        ),
    ]
