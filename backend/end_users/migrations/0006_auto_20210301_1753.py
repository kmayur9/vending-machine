# Generated by Django 3.1.7 on 2021-03-01 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('end_users', '0005_auto_20210301_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='value',
            new_name='Order_Value',
        ),
        migrations.RemoveField(
            model_name='order',
            name='orderProduct',
        ),
        migrations.AddField(
            model_name='order',
            name='Date',
            field=models.DateField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='OrderProduct',
        ),
    ]
