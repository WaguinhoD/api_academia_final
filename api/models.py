from django.db import models
from django.utils.text import slugify

# Create your models here.


class Instrutor(models.Model):
    nome = models.CharField(max_length=100, )
    sobrenome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="uploads/instrutoresImages", blank=True,
                             null=True)
    descricao = models.TextField(blank=True, null=True)
    slug_name = models.SlugField(unique=True, blank=True, primary_key=True)

    def save(self, *args, **kwargs):
        self.slug_name = slugify(f'{self.nome} {self.sobrenome}')
        if not self.foto:
            try:
                instance = Instrutor.objects.get(pk=self.pk)
                self.foto = instance.foto
            except:
                pass

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'


class Plano(models.Model):
    image_plano = models.ImageField(upload_to="uploads/planoImages",
                                    blank=True,
                                    null=True)
    nome_plano = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    beneficio1 = (models.CharField(max_length=300, blank=True, null=True))
    beneficio2 = (models.CharField(max_length=300, blank=True, null=True))
    beneficio3 = (models.CharField(max_length=300, blank=True, null=True))
    beneficio4 = (models.CharField(max_length=300, blank=True, null=True))
    beneficio5 = (models.CharField(max_length=300, blank=True, null=True))

    def save(self, *args, **kwargs):
        if not self.image_plano:
            try:
                instance = Plano.objects.get(pk=self.pk)
                self.image_plano = instance.image_plano
            except:
                pass

        super().save(*args, **kwargs)

    def __int__(self):
        return self.id


class Programa(models.Model):
    image_programa = models.ImageField(upload_to="uploads/programaImages",
                                       blank=True,
                                       null=True)
    nome_programa = models.CharField(max_length=100)
    descricao = (models.TextField(blank=True, null=True))

    def save(self, *args, **kwargs):
        if not self.image_programa:
            try:
                instance = Programa.objects.get(pk=self.pk)
                self.image_programa = instance.image_programa
            except:
                pass

        super().save(*args, **kwargs)

    def __int__(self):
        return self.id
