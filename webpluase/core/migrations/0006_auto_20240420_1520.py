# Generated by Django 2.2.14 on 2024-04-20 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20240420_0904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='item',
            new_name='items',
        ),
    ]