# Generated by Django 4.2.5 on 2023-10-17 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_remove_place_description_long_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('position', models.PositiveIntegerField(db_index=True, default=0, verbose_name='Position')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place', verbose_name='Place')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]