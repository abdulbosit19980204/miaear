# Generated by Django 5.0.6 on 2024-05-19 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_entities_name_alter_entities_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entities',
            name='date',
            field=models.DateTimeField(),
        ),
    ]