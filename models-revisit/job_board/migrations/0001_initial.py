# Generated by Django 5.0.6 on 2024-06-03 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('company', models.CharField(max_length=255)),
                ('salary', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
