# Generated by Django 3.2.9 on 2022-09-01 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listing',
            options={'ordering': ('-created_at',)},
        ),
    ]