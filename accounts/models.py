#-*- coding: UTF-8 -*- 
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
##for img ,upload,resize
from stdimage import StdImageField

class MyProfile(UserenaBaseProfile):
    courier=models.BooleanField(u'快递员',default=False)
    user = models.OneToOneField(User,unique=True,verbose_name=_('user'),related_name='my_profile')
    GENDER_CHOICES = ((1, _('Male')),(2, _('Female')),)
    gender = models.PositiveSmallIntegerField(_('gender'),choices=GENDER_CHOICES,blank=True,null=True)
    date_joined=models.DateTimeField(u'注册时间',auto_now_add=True)
    eal_name=models.CharField(u'真实姓名',max_length=100,blank=True)
    major=models.CharField(u'专业',max_length=100,blank=True)
    address=models.CharField(u'住址',max_length=100,blank=True)
    identity_card=models.CharField(u'身份证',max_length=100,blank=True)
    student_number=models.CharField(u'学号',max_length=100,blank=True)
    #one_card=models.FileField(u'一卡通',null=True,blank=True,upload_to='onecard')
    one_card=StdImageField(u'一卡通',upload_to='onecard', variations={'thumbnail': (100, 75)},blank=True) # creates a thumbnail resized to maximum size to fit a 100x75 area
    #favourite_snack = models.CharField(_('favourite snack'),max_length=5)

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