# Generated by Django 4.0.5 on 2022-06-23 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='boleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nroBoleta', models.IntegerField()),
                ('cantidadProductos', models.IntegerField()),
                ('total', models.FloatField()),
                ('fecha', models.DateField()),
            ],
        ),
    ]