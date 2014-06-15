#-*- coding: UTF-8 -*- 
from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here

class Kuaijian(models.Model):
            b=((u'已送达',u'已送达'),(u'未送达',u'未送达'))
            songda=models.CharField(u'送达',max_length=20,choices=b,default=u'未送达')
            bianhao=models.CharField(max_length=30,unique=True)
            name=models.CharField(max_length=100)
            description=UEditorField(u'内容',height=100,width=500,default='test',imagePath="uploadimg/",imageManagerPath="imglib",toolbars='large',options={"elementPathEnabled":True},filePath='upload',blank=True)
            upTime=models.DateTimeField(u'上传时间',auto_now_add=True)
            c=((u'服务中心',u'服务中心'),(u'北门',u'北门'),(u'南门',u'南门'))
            place=models.CharField(u'取货地点',max_length=20,choices=c,default=u'服务中心')
            def __unicode__(self):
                return ("%s--- %s"%(self.name,self.upTime))
            class Meta:
                 verbose_name_plural=u'快件'
	    ordering=['-upTime']

class MyCounter(models.Model):
            upcount=models.IntegerField()
            songdacount=models.IntegerField()
            date=models.DateField()

            class Meta:
                verbose_name_plural=u'快件计数器'
                ordering=['-date']
        




'''
Action 插件在数据列表页面提供了数据选择功能, 
选择后的数据可以经过 Action 做特殊的处理.
 默认提供的 Action 为批量删除功能.
'''
from xadmin.plugins.actions import BaseActionView
#from django.http import HttpResponse
#from django.shortcuts import render
from django.http import HttpResponseRedirect

class Songda(BaseActionView):

        # 这里需要填写三个属性
        action_name = "songda"    #: 相当于这个 Action 的唯一标示, 尽量用比较针对性的名字
        description = (u'标为送达') #: 描述, 出现在 Action 菜单中, 可以使用 ``%(verbose_name_plural)s`` 代替 Model 的名字.

        model_perm = 'change'    #: 该 Action 所需权限

    # 而后实现 do_action 方法
        def do_action(self, queryset):
            # queryset 是包含了已经选择的数据的 queryset
            for obj in queryset:
                # obj 的操作
                obj.songda='已送达'
                obj.save()
            # 返回 HttpResponse
            #return HttpResponseRedirect('/%s'%self.admin_site.name.app)
            return HttpResponseRedirect('/xadmin/chuangxing/kuaijian/')