# Generated by Django 2.2.5 on 2019-09-07 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('requisiciones', '0002_auto_20190907_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisicion',
            name='cotizacion',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='requisiciones.Cotizacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requisicion',
            name='estatus',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='requisiciones.RequesicionEstatus'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requisicion',
            name='tipo',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='requisiciones.RequesicionTipo'),
            preserve_default=False,
        ),
    ]