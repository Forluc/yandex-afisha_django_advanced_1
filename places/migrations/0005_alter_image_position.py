# Generated by Django 4.2.5 on 2023-10-18 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_alter_place_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=0, verbose_name='Position'),
        ),
    ]
