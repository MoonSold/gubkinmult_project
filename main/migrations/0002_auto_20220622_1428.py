# Generated by Django 3.2.9 on 2022-06-22 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='long_mult',
            options={'verbose_name': 'Мультик', 'verbose_name_plural': 'Длинные мультики'},
        ),
        migrations.RenameField(
            model_name='long_mult',
            old_name='season',
            new_name='mult',
        ),
    ]
