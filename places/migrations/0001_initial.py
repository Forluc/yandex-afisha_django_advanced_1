# Generated by Django 4.2.5 on 2023-10-08 17:49

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description_short', models.TextField(verbose_name='description_short')),
                ('description_long', tinymce.models.HTMLField(verbose_name='description_long')),
                ('latitude', models.FloatField(verbose_name='latitude')),
                ('longitude', models.FloatField(verbose_name='longitude')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('image', models.ImageField(upload_to='')),
                ('position', models.AutoField(primary_key=True, serialize=False)),
                ('place', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place', verbose_name='Place')),
            ],
        ),
    ]
