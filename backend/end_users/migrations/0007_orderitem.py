# Generated by Django 3.1.7 on 2021-03-01 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('end_users', '0006_auto_20210301_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('Order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='end_users.order')),
                ('Product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='end_users.product')),
            ],
        ),
    ]
