# Generated by Django 3.2.6 on 2021-09-02 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0005_auto_20210902_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='payworkshop',
            name='order_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
