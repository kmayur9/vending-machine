# Generated by Django 3.1.7 on 2021-02-24 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('end_users', '0002_auto_20210224_0014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Denomination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=255)),
                ('val', models.IntegerField()),
            ],
        ),
    ]
