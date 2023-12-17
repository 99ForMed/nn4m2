# Generated by Django 4.1.5 on 2023-12-17 04:37

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0011_alter_entrysubmission_atar_alter_entrysubmission_gpa'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrysubmission',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, max_length=128, null=True, region='AU'),
        ),
    ]
