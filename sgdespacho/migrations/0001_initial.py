# Generated by Django 3.0.6 on 2020-06-27 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('categoria', models.CharField(max_length=255)),
                ('precio', models.IntegerField()),
                ('fecha', models.DateField()),
            ],
        ),
    ]