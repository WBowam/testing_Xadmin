#-*- coding: UTF-8 -*- 
#from django.contrib import admin

# Register your models here.
import xadmin
from models import Kuaijian,Songda,MyCounter


class KuaijianAdmin(object):
	#search_fields=('name','category','content')
	actions = [Songda, ]
	list_display = ('id','name', "bianhao",  "place",'upTime','songda')
	list_display_links = ('id','name', "bianhao",  "place",'upTime','songda')
	ordering = ("-upTime",)
	list_filter=('place','upTime','songda')#该属性指定可以过滤的列的名字, 系统会自动生成搜索器
	search_fields=('name','place','bianhao')#属性指定可以通过搜索框搜索的数据列的名字, 搜索框搜索使用的是模糊查找的方式, 一般用来搜素名字等字符串字段
	


class MyCounterAdmin(object):
	data_charts ={
	"upcount Report": {'title': u"上传快件情况", "x-field": "date", "y-field": ("upcount", "songdacount")},
	"songdacount Report": {'title': u"送达快件情况", "x-field": "date", "y-field": ('songdacount',),}
	}
	'''
	图表的主要属性为:

		title : 图表的显示名称

		x-field : 图表的 X 轴数据列, 一般是日期, 时间等

		y-field : 图表的 Y 轴数据列, 该项是一个 list, 可以同时设定多个列, 这样多个列的数据会在同一个图表中显示

		order : 排序信息, 如果不写则使用数据列表的排序
	'''

xadmin.site.register(Kuaijian,KuaijianAdmin)
xadmin.site.register(MyCounter,MyCounterAdmin)