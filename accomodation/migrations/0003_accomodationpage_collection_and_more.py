# Generated by Django 5.0.6 on 2024-07-21 14:32

import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accomodation', '0002_remove_roomtype_image_roomtype_images_and_more'),
        ('wagtailcore', '0093_uploadedfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='accomodationpage',
            name='collection',
            field=models.ForeignKey(blank=True, help_text='Select the image collection for this gallery.', limit_choices_to=models.Q(('name__in', ['Root']), _negated=True), null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.collection'),
        ),
        migrations.AlterField(
            model_name='accomodationpage',
            name='feature_description_one',
            field=wagtail.fields.StreamField([('feature', wagtail.blocks.StructBlock([('description', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'link'], help_text='Description of the first accommodation feature'))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='accomodationpage',
            name='feature_description_two',
            field=wagtail.fields.StreamField([('feature', wagtail.blocks.StructBlock([('description', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'link'], help_text='Description of the first accommodation feature'))]))], blank=True, null=True),
        ),
    ]
