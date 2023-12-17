# Generated by Django 4.1.5 on 2023-12-17 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0013_entrysubmission_submitted_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='UcatCourseDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_letter', models.TextField()),
                ('subtext', models.CharField(max_length=400)),
                ('title', models.CharField(max_length=400)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('course_start', models.DateField()),
                ('course_end', models.DateField()),
            ],
            options={
                'verbose_name': 'Entry Submission',
                'verbose_name_plural': 'Entry Submissions',
            },
        ),
    ]
