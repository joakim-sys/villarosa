# Generated by Django 5.0.6 on 2024-07-21 15:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accomodation', '0006_accomodationpage_floor_layout_doc'),
        ('wagtaildocs', '0013_delete_uploadeddocument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accomodationpage',
            name='floor_layout_doc',
            field=models.ForeignKey(blank=True, help_text='Select the floor layout document.', limit_choices_to=models.Q(('name__in', ['Root']), _negated=True), null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtaildocs.document'),
        ),
    ]
