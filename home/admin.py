# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import *


admin.site.site_header = 'Site Administrativo da RNJunior'

class ClienteNewsletterAdmin(admin.ModelAdmin):

	list_display = ['nome', 'email']
	search_fields = ['nome', 'email']
	list_filter = ['nome']


class NoticiasAdmin(admin.ModelAdmin):

	search_fields = ['texto']
	exclude = ( 'data_orientation', 'data_slice_1', 
		'data_slice_2', 'data_slice_1_scale', 'data_slice_2_scale',
		)
	#Esse campo indica que quando você escrever o campo 'título', o campo
	#'slug' será escrito com o valor de 'título' sem caracteres especiais
	#ou espaços
	prepopulated_fields = {'slug': ('titulo',)}


class ParceirosAdmin(admin.ModelAdmin):

	search_fields = ['titulo', 'texto']


class SetoresAdmin(admin.ModelAdmin):

	search_fields = ['setor']


class EmpresasAdmin(admin.ModelAdmin):

	search_fields = ['nome_empresa']


admin.site.register(ClienteNewsletter, ClienteNewsletterAdmin)
admin.site.register(Noticias, NoticiasAdmin)
admin.site.register(Parceiros, ParceirosAdmin)
admin.site.register(AreaModel)
admin.site.register(SetorModel, SetoresAdmin)
admin.site.register(EmpresaModel, EmpresasAdmin)
admin.site.register(Diretor)
admin.site.register(Assessores)
admin.site.register(Eventos)
admin.site.register(TextoRN)