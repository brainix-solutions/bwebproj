# Generated by Django 3.2.6 on 2021-09-02 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0004_payment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='payment',
        ),
        migrations.AddField(
            model_name='payworkshop',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='payworkshop',
            name='razorpay_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
