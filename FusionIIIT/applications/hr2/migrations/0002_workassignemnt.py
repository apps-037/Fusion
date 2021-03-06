# Generated by Django 3.1.5 on 2021-05-09 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0003_auto_20191024_1242'),
        ('hr2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkAssignemnt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, max_length=6, null=True)),
                ('end_date', models.DateField(blank=True, max_length=6, null=True)),
                ('job_title', models.CharField(default='', max_length=50)),
                ('orders_copy', models.FileField(blank=True, null=True, upload_to='')),
                ('extra_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
        ),
    ]
