# Generated by Django 3.0.5 on 2021-03-30 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=500)),
                ('phone_number', models.CharField(max_length=10)),
                ('hire_date', models.CharField(max_length=10)),
                ('job_id', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('commission_pct', models.IntegerField()),
                ('manager_id', models.IntegerField()),
                ('department_id', models.IntegerField()),
                ('image', models.ImageField(blank=True, default=None, upload_to='')),
            ],
        ),
    ]
