# Generated by Django 4.2 on 2023-04-15 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.TextField()),
                ('date', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.staff')),
            ],
        ),
    ]
