# Generated by Django 3.2.6 on 2021-08-16 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0002_payworkshop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedbackform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('subject', models.CharField(max_length=200, null=True)),
                ('message', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
