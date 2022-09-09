# Generated by Django 4.1 on 2022-09-09 09:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_skill_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('answer', models.CharField(choices=[('backend', 'backend'), ('frontend', 'frontend'), ('fullstack', 'fullstack')], max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
