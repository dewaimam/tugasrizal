# Generated by Django 5.0.3 on 2024-03-22 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='perpus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=30)),
                ('alamat', models.TextField()),
                ('npm', models.CharField(max_length=30)),
                ('profesi', models.CharField(max_length=30)),
            ],
        ),
    ]
