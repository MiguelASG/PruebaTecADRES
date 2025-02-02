# Generated by Django 5.0.6 on 2024-06-27 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presupuesto', models.BigIntegerField()),
                ('unidad', models.CharField(max_length=100)),
                ('TipoBien', models.CharField(max_length=50)),
                ('Cantidad', models.IntegerField()),
                ('ValorUnit', models.BigIntegerField()),
                ('ValorTot', models.BigIntegerField()),
                ('Fecha', models.DateField()),
                ('Proveedor', models.CharField(max_length=60)),
                ('Documen', models.TextField(max_length=200)),
            ],
        ),
    ]
