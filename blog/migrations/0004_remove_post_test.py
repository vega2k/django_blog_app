# Generated by Django 2.1.1 on 2018-09-30 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='test',
        ),
    ]
