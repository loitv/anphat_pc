# Generated by Django 2.2.3 on 2019-08-25 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laptop',
            old_name='cpu_id',
            new_name='cpu',
        ),
        migrations.RenameField(
            model_name='laptop',
            old_name='ram_id',
            new_name='ram',
        ),
        migrations.RenameField(
            model_name='laptop',
            old_name='vga_id',
            new_name='vga',
        ),
    ]
