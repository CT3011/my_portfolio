# Generated by Django 4.1 on 2022-09-06 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_comment_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='logo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
