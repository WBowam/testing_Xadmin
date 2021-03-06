#-*- coding: UTF-8 -*- 
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
#from DjangoUeditor.models import UEditorField
import datetime

# Create your models here


class Kuaijian(models.Model):
            created_by = models.ForeignKey(User,verbose_name=_('user'),related_name='kuaijian')
            b=((u'已送达',u'已送达'),(u'未送达',u'未送达'))
            delivered=models.CharField(u'送达情况',max_length=20,choices=b,default=u'未送达')
            f=((u'已代取',u'已代取'),(u'未代取',u'未代取'))
            bought=models.CharField(u'代取情况',max_length=20,choices=f,default=u'未代取')
            a=((u'圆通',u'圆通'),(u'EMS',u'EMS'),(u'汇通',u'汇通'),(u'申通',u'申通'),(u'圆通',u'圆通'),(u'顺丰',u'顺丰'),(u'邮政小包',u'邮政小包'),(u'韵达',u'韵达'),(u'天天快递',u'天天快递'))
            express=models.CharField(u'快递公司',max_length=100,choices=a,default=u'申通')
            c=((u'服务中心',u'服务中心'),(u'北门',u'北门'),(u'南门',u'南门'))
            sourcePosition=models.CharField(u'取货地点',max_length=20,choices=c,default=u'服务中心')
            destinationPosition=models.CharField(u'送货地点',max_length=500)
            name=models.CharField(u'收件人名字 ',max_length=200,blank=True)
            #upUser=models.ForeignKey(User)
            getBeginTime=models.DateTimeField(u'快件代取时间(开始)',default=datetime.datetime.now)
            getEndTime=models.DateTimeField(u'快件代取时间(结束)')
            h=((u'当日',u'当日'),(u'两天内',u'两天内'),(u'三天内',u'三天内'))
            deadLine=models.CharField(u'快件配送期限',max_length=20,choices=h,default=u'当日',help_text="从创建快件需求的时间开始计时Please use the following format: <em>YYYY-MM-DD</em>.")
            #postBeginTime=models.DateTimeField(u'快件送货时间(开始)')
            #postEndTime=models.DateTimeField(u'快件送货时间(结束)')
            #bianhao=models.CharField(max_length=30,unique=True)
            d=((u'小于1公斤重',u'小于1公斤重'),(u'小于5公斤重',u'小于5公斤重'),(u'小于10公斤重',u'小于10公斤重'),(u'小于50公斤重',u'小于50公斤重'))
            goodsWeight=models.CharField(u'快件重量',max_length=50,choices=d,default='小于1公斤重',blank=True,help_text=u"代取小费参考价：起步价1元，每公斤增加0.5元")
            e=((u'信件',u'信件'),(u'书籍',u'书籍'),(u'衣服',u'衣服'),(u'鞋子',u'鞋子'),(u'其他',u'其他'))
            goodsVariety=models.CharField(u'快件种类',max_length=50,choices=e,default='信件',blank=True)
            message=models.TextField(u'备注',blank=True)
            upTime=models.DateTimeField(u'上传时间',auto_now_add=True)
            #,error_messages={'required': '别这么小气嘛，不给小费人家怎么给你送嘛'}
            tip=models.CharField(max_length=20)
            
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
                obj.delivered='已送达'
                obj.save()
            # 返回 HttpResponse
            #return HttpResponseRedirect('/%s'%self.admin_site.name.app)
            return HttpResponseRedirect('/xadmin/chuangxing/kuaijian/')