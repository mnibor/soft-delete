# Generated by Django 4.2.6 on 2023-10-27 00:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('deleted', models.BooleanField(default=False, verbose_name='Eliminado')),
                ('deleted_date', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de eliminación')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='Slug')),
                ('body', models.TextField(verbose_name='Contenido')),
                ('deleted', models.BooleanField(default=False, verbose_name='Eliminado')),
                ('deleted_date', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de eliminación')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category', verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'Publicación',
                'verbose_name_plural': 'Publicaciones',
                'ordering': ['-id'],
            },
        ),
    ]