#-*- coding: UTF-8 -*- 
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
##for img ,upload,resize
from stdimage import StdImageField
##for phone
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class ReceiveAddress(models.Model):
    user=models.ForeignKey(User,verbose_name=_('user'),related_name='receive_address')
    campus_CHOICES=((u'华电二校',u'华电二校'),)
    campus=models.CharField(u'校区',choices=campus_CHOICES,max_length=20,default=u'华电二校')
    buildings_CHOICES=((u'6舍',u'6舍'),(u'7舍',u'7舍'),(u'8舍',u'8舍'),(u'9舍',u'9舍'),(u'10舍',u'10舍'),(u'11舍',u'11舍'),(u'12舍',u'12舍'),(u'13舍',u'13舍'),(u'15舍',u'15舍'),(u'16舍',u'16舍'),(u'17舍',u'17舍'),(u'18舍',u'18舍'))
    buildings=models.CharField(u'楼宇',choices=buildings_CHOICES,max_length=20,default=u'6舍')
    room=models.CharField(u'房间',max_length=5,blank=True)
    #user=models.OneToOneField(User,unique=True,verbose_name=_('user'),related_name='receive_address')

    def __unicode__(self):
        return ("%s %s %s"%(self.campus,self.buildings,self.room))
    
    class Meta:
        verbose_name_plural=u'收货地址'
        #app_label=u'助学贷款'
        #ordering=["-date_joined"]


class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,unique=True,verbose_name=_('user'),related_name='my_profile')
    user_state_CHOICES=((u'普通用户',u'普通用户'),(u'高级用户',u'高级用户'),(u'快递人',u'快递人'))
    user_state=models.CharField(u'用户状态',max_length=20,choices=user_state_CHOICES,default=u'普通用户')
    GENDER_CHOICES = ((1, _('Male')),(2, _('Female')),)
    gender = models.PositiveSmallIntegerField(_('gender'),choices=GENDER_CHOICES,blank=True,null=True)
    date_joined=models.DateTimeField(u'注册时间',auto_now_add=True)
    real_name=models.CharField(u'真实姓名',max_length=100)
    #major=models.CharField(u'专业',max_length=100,blank=True)
    #address=models.ForeignKey(ReceiveAddress,verbose_name=u'收货地址',related_name='my_profile',help_text=u"目前只支持华电二校范围")
    #address=models.CharField(u'住址',max_length=100,blank=True)
    #phone=models.PositiveSmallIntegerField()
    phone = models.CharField(max_length=11,blank=True,validators=[RegexValidator(regex='^\d{11}$', message='请输入正确的手机号', code='Invalid number')])
    #identity_card=models.CharField(u'身份证',max_length=100,blank=True)
   # student_number=models.CharField(u'学号',max_length=100,blank=True)
    #one_card=models.FileField(u'一卡通',null=True,blank=True,upload_to='onecard')
    one_card=StdImageField(u'一卡通',upload_to='onecard', variations={'thumbnail': (100, 75)},blank=True) # creates a thumbnail resized to maximum size to fit a 100x75 area

    def image_img(self):
        if self.one_card:
            return str('<img src="%s" />' % self.one_card.thumbnail.url)
        else:
            return u'上传一卡通'
    image_img.short_description = '一卡通'
    image_img.allow_tags = True
    def image_img2(self):
        if self.mugshot:
            return str('<img src="%s" />' % self.mugshot.url)
        else:
            return u'上传头像'
    image_img2.short_description = '头像'
    image_img2.allow_tags = True

    class Meta:
        verbose_name_plural=u'个人资料'
        #app_label=u'助学贷款'
        ordering=["-date_joined"]