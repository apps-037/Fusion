# Generated by Django 3.0.8 on 2020-07-09 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0017_questionaccesscontrol_posted_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionaccesscontrol',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='question_list', to='feeds.AskaQuestion'),
        ),
    ]
