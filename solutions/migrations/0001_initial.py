# Generated by Django 3.2.6 on 2021-08-13 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trialworkshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200, null=True)),
                ('lname', models.CharField(max_length=200, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=200, null=True)),
                ('pname', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('phno', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('spref', models.CharField(choices=[('1:1', '1:1'), ('1:5', '1:5')], max_length=200, null=True)),
                ('lpref', models.CharField(choices=[('English', 'English'), ('Tamil', 'Tamil'), ('Malayalam', 'Malayalam')], max_length=200, null=True)),
            ],
        ),
    ]
