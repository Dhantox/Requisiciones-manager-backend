# Generated by Django 2.2.5 on 2019-09-11 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('requisiciones', '0007_auto_20190910_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisicionestado',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='requisiciones.CategoriaEstado'),
        ),
    ]