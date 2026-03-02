from PIL.ImageOps import crop
from django.db import models
from stdimage import StdImageField
import uuid
import os

class Base(models.Model):
    criado = models.DateTimeField('Criação', auto_now_add=True)
    modificado = models.DateTimeField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True

class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem' ),
        ('lni-stats-up', 'Gráfico' ),
        ('lni-users', 'Usuários' ),
        ('lni-layers', 'Design' ),
        ('lni-mobile', 'Móbile' ),
        ('lni-rocket', 'Foguete' ),
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.CharField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=13, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico

class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('images', filename)

class Colaborador(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    descricao = models.TextField('Descrição', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'

    def __str__(self):
        return self.nome

class Caracteristica(Base):
    ICONES_CHOICES = (
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Laptop/Phone'),
        ('lni-cog','Engrenagem'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Folhas de papel')
    )

    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descricao', max_length=200)
    icone = models.CharField('Icone', max_length=17, choices=ICONES_CHOICES)

    class Meta:
        verbose_name = 'Caracteristica'
        verbose_name_plural = 'Caracteristicas'

    def __str__(self):
        return self.nome

class Preco(Base):

    TIPO_CHOICES = (
        ('PRO', 'Pro'),
        ('PLUS', 'Plus'),
        ('PREMIUM', 'Premium'),
    )

    ICONE_CHOICES = (
        ('lni-package', 'Caixa'),
        ('lni-star', 'Estrela'),
        ('lni-drop', 'Gota')
    )

    ATENDIMENTO_CHOICES = (
        ('Atendimento por e-mail', 'Atendimento por e-mail'),
        ('Atendimento priotário por e-mail', 'Atendimento priotário por e-mail'),
        ('Atendimento 24 horas', 'Atendimento 24 horas/dia'),
    )

    icone = models.CharField('Icone', max_length=13, choices=ICONE_CHOICES)
    preco = models.IntegerField('Preço', default=0)
    servico = models.CharField('Serviço', max_length=10, choices=TIPO_CHOICES)
    usuario = models.IntegerField('Quantidade de usuários')
    armazenamento = models.IntegerField('Armazenamento')
    atendimento = models.CharField('Atendimento', max_length=35, choices=ATENDIMENTO_CHOICES)

    class Meta:
        verbose_name = 'Preço'
        verbose_name_plural = 'Preços'

    def __str__(self):
        return self.servico

