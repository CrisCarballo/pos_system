# Generated by Django 3.2.12 on 2023-09-29 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_alter_customer_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='lastName',
            new_name='last_name',
        ),
    ]