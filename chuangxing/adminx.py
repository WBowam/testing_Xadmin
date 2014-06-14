#-*- coding: UTF-8 -*- 
#from django.contrib import admin

# Register your models here.
import xadmin
from models import Kuaijian,Songda


class KuaijianAdmin(object):
	#search_fields=('name','category','content')
	list_display = ('id','name', "bianhao",  "place",'upTime','songda')
	list_display_links = ('id','name', "bianhao",  "place",'upTime','songda')
	ordering = ("-upTime",)

	actions = [Songda, ]

xadmin.site.register(Kuaijian,KuaijianAdmin)