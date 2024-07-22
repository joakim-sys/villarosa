# Generated by Django 5.0.6 on 2024-07-20 08:09

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_service_cta_link_service_cta_text'),
        ('wagtailcore', '0093_uploadedfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='IconLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(choices=[('e_fas_swimmer', 'Swimmer'), ('e_fas_biking', 'Biking'), ('e_fas_car_alt', 'Car'), ('e_fas_bus', 'Bus'), ('e_fas_glass_cheers', 'Glass Cheers'), ('e_fas_atom', 'Atom')], max_length=255)),
                ('cta_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='icon_links', to='home.homepage')),
            ],
        ),
    ]
