# Generated by Django 2.2.5 on 2019-09-09 22:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('requisiciones', '0005_auto_20190909_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaEstado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=255)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RequisicionEstado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon', models.TextField()),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('cateogoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requisiciones.CategoriaEstado')),
                ('usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='requisicion',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='requisiciones.RequisicionEstado'),
        ),
    ]
