# Generated by Django 2.2.9 on 2020-01-22 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200122_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Friend')),
            ],
        ),
    ]