# Generated by Django 5.0.6 on 2024-07-20 08:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_rename_cta_link_iconlink_link_iconlink_title'),
        ('wagtailcore', '0093_uploadedfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='styled_link_text',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='styled_link_text_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
    ]
