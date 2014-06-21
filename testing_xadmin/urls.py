from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import xadmin
xadmin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^fwzx$', 'chuangxing.views.fwzx', name='fwzx'),
    url(r'^bm$', 'chuangxing.views.bm', name='bm'),
    url(r'^nm$', 'chuangxing.views.nm', name='nm'),
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
    # url(r'^blog/', include('blog.urls')),

    url(r'^xadmin/', include(xadmin.site.urls), name='xadmin'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    ##for userena
    (r'^accounts/', include('userena.urls')),
)




from django.conf import settings
urlpatterns += patterns('',
	url(r"^static/(?P<path>.*)$","django.views.static.serve",{"document_root": settings.STATIC_ROOT,}),
	)


##added by Tulpar,20140514
#from django.conf import settings

urlpatterns += patterns('',
    url(r"^media/(?P<path>.*)$","django.views.static.serve",{"document_root": settings.MEDIA_ROOT,}),
)