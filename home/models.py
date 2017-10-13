from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse

from ckeditor.fields import RichTextField


#Modelo responsável por salvar o pessoal no Newsletter
class ClienteNewsletter(models.Model):

    nome = models.CharField("Nome", max_length=100)
    email = models.EmailField("E-mail")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Newsletter"
        verbose_name_plural = "08 - Newsletter"


#Cadastra as notícias e joga no SlideShow
class Noticias(models.Model):

    titulo = models.CharField(max_length=100, unique=True)
    texto = models.CharField("Texto", max_length=100)
    texto_teste = RichTextField()
    slug = models.SlugField("Link", max_length=100, unique=True, help_text="Link da notícia. Não usar caracteres com acentos ou caracteres especiais.")
    imagem = models.ImageField("Imagem", upload_to="noticias/%y/%m/%d")
    modificado = models.BooleanField(default=False)
    data_orientation = models.CharField(max_length=100, blank=True)
    data_slice_1 = models.SmallIntegerField(blank=True, null=True)
    data_slice_2 = models.SmallIntegerField(blank=True, null=True)
    data_slice_1_scale = models.FloatField(blank=True, null=True)
    data_slice_2_scale = models.FloatField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('noticia', kwargs={'slug': self.slug})

    def noticia_save(self, valor_string, valor1, valor2, valor3, valor4):
        self.data_orientation = valor_string
        self.data_slice_1 = valor1
        self.data_slice_2 = valor2
        self.data_slice_1_scale = valor3
        self.data_slice_2_scale = valor4
        self.modificado = True

    #Sobrescrevi o método save padrão do modelo para que
    #quando uma nova instância fosse criada e salva,
    #fosse enviado um email a todos os inscritos no Newsletter
    def save(self, *args, **kwargs):
        listaDosEmails = []
        for i in ClienteNewsletter.objects.all():
            listaDosEmails.append(i.email)
        send_mail(
            "Nome do camarada",
            self.texto,
            settings.DEFAULT_FROM_EMAIL,
            listaDosEmails,
            fail_silently=False,
        )
        self.noticia_save("vertical", 10, -15, 1.5, 1.5)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.texto[:100]

    class Meta:
        verbose_name = "Notícia"
        verbose_name_plural = "01 - Notícias"


#Modelo para salvar os parceiros
class Parceiros(models.Model):

    foto = models.ImageField("Imagem", upload_to="parceiros/%y/%m/%d")
    titulo = models.CharField("Título", max_length=100)
    texto = models.TextField("Texto")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Parceiro"
        verbose_name_plural = "05 - Parceiros"


class AreaModel(models.Model):

    area = models.CharField("Área", max_length=100)

    def __str__(self):
        return self.area

    def nome_formatado(self):
        return self.area.replace(" ", "-").lower()

    class Meta:
        verbose_name = "Área"
        verbose_name_plural = "02 - Áreas"


class SetorModel(models.Model):

    setor = models.CharField("Setor", max_length=100)
    area_referencia = models.ForeignKey(AreaModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.setor

    def nome_formatado(self):
        return self.setor.replace(" ", "-").lower()

    class Meta:
        verbose_name = "Setor"
        verbose_name_plural = "03 - Setores"


class EmpresaModel(models.Model):

    nome_empresa = models.CharField("Nome da empresa", max_length=100)
    foto_empresa = models.ImageField("Foto da empresa", upload_to="empresa/%y/%m/%d")
    email_empresa = models.EmailField("E-mail da empresa")
    setor_referencia = models.ManyToManyField(SetorModel)

    def __str__(self):
        return self.nome_empresa

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "04 - Empresas"


class Diretor(models.Model):

    nome = models.CharField("Nome do diretor", max_length=200)
    cargo = models.CharField("Cargo", max_length=150)
    foto = models.ImageField("Foto do diretor", upload_to="diretor/%y/%m/%d")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Diretor"
        verbose_name_plural = "06 - Diretores"


class Assessores(models.Model):

    nome = models.CharField("Nome do assessor", max_length=200)
    foto = models.ImageField("Foto do assessor", upload_to="assessor/%y/%m/%d")
    diretor_referencia = models.ForeignKey(Diretor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Assessor"
        verbose_name_plural = "07 - Assessores"