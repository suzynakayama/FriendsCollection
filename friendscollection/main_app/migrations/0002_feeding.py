# Generated by Django 2.2.9 on 2020-01-22 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('drink', models.CharField(choices=[('B', 'Beer'), ('S', 'Sake'), ('T', 'Tequila'), ('V', 'Vodka'), ('W', 'Wine')], default='B', max_length=1)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Friend')),
            ],
        ),
    ]
