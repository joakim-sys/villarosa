# Generated by Django 5.0.6 on 2024-07-21 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accomodation', '0003_accomodationpage_collection_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accomodationpage',
            old_name='collection',
            new_name='look_around_gallery',
        ),
        migrations.RemoveField(
            model_name='accomodationpage',
            name='image_gallery_one',
        ),
        migrations.RemoveField(
            model_name='accomodationpage',
            name='image_gallery_two',
        ),
    ]
