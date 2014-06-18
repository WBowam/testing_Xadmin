#-*- coding: UTF-8 -*- 
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,unique=True,verbose_name=_('user'),related_name='my_profile')
    # GENDER_CHOICES = ((1, _('Male')),(2, _('Female')),)
    # gender = models.PositiveSmallIntegerField(_('gender'),choices=GENDER_CHOICES,blank=True,null=True)
    # #date_joined=models.DateTimeField(u'注册时间',auto_now_add=True)
    #real_name=models.CharField(u'真实姓名',max_length=100,blank=True)
    #major=models.CharField(u'专业',max_length=100,blank=True)
    #address=models.CharField(u'住址',max_length=100,blank=True)
    #identity_card=models.CharField(u'身份证',max_length=100,blank=True)
    #student_number=models.CharField(u'学号',max_length=100,blank=True)
    #one_card=models.FileField(u'一卡通',null=True,blank=True,upload_to='onecard')
    favourite_snack = models.CharField(_('favourite snack'),max_length=5)