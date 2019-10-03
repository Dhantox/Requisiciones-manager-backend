# Generated by Django 2.2.5 on 2019-10-02 04:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('requisiciones', '0014_auto_20190925_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompraRapida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo', models.FloatField()),
                ('proveedores', models.CharField(max_length=250)),
                ('fecha_creacion', models.DateTimeField()),
                ('usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='requisicion',
            name='compra_rapida',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='requisiciones.CompraRapida'),
        ),
    ]