# Generated by Django 3.2.8 on 2021-10-25 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trading_logic', '0006_auto_20211025_1421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='item',
            new_name='items',
        ),
    ]
