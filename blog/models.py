from django.db import models
from slugify import slugify

from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    deleted = models.BooleanField(default=False, verbose_name='Eliminado')
    deleted_date = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de eliminación')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    slug = models.SlugField(unique=True, blank=True, verbose_name='Slug')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Categoría')
    body = models.TextField(verbose_name='Contenido')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Autor')
    deleted = models.BooleanField(default=False, verbose_name='Eliminado')
    deleted_date = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de eliminación')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-id']

    def __str__(self):
        return self.title