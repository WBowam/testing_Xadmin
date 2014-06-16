#-*- coding: UTF-8 -*- 
from django.contrib import admin
from models import Kuaijian

class KuaijianAdmin(admin.ModelAdmin):
	#exclude = ('author',)

	def save_model(self, request, obj, form, change):
	    if not change:
	        obj.name = request.user
	    obj.save()



admin.site.register(Kuaijian,KuaijianAdmin)