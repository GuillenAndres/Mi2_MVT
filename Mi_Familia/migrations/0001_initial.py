# Generated by Django 4.1 on 2022-08-29 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdr_nombre', models.CharField(max_length=40)),
                ('pdr_edad', models.FloatField()),
                ('pdr_nacimiento', models.DateField()),
                ('mdr_nombre', models.CharField(max_length=40)),
                ('mdr_edad', models.FloatField()),
                ('mdr_nacimiento', models.DateField()),
                ('hjs_nombre', models.CharField(max_length=40)),
                ('hjs_edad', models.FloatField()),
                ('hjs_nacimiento', models.DateField()),
            ],
        ),
    ]