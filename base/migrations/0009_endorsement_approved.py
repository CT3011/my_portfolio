# Generated by Django 4.1 on 2022-09-05 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_endorsement'),
    ]

    operations = [
        migrations.AddField(
            model_name='endorsement',
            name='approved',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
