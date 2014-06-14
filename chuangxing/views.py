#-*- coding: UTF-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse
from models import Kuaijian
# Create your views here.
def bm(request):
	i=1
	while i<100:

		k=Kuaijian(bianhao=str(i),name='快件'+str(i),place='bm')
		k.save()
		i=i+1
	return HttpResponse('1 -100 bm shuju')


def nm(request):
	i=100
	while i<200:

		k=Kuaijian(bianhao=str(i),name='快件'+str(i),place='nm')
		k.save()
		i=i+1
	return HttpResponse('100 -200  nm shuju')


def fwzx(request):
	i=200
	while i<300:

		k=Kuaijian(bianhao=str(i),name='快件'+str(i),place='fwzx')
		k.save()
		i=i+1
	return HttpResponse('200 -300 fwzx shuju')