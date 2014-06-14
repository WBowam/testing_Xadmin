from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()
import xadmin
xadmin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^fwzx$', 'chuangxing.views.fwzx', name='fwzx'),
    url(r'^bm$', 'chuangxing.views.bm', name='bm'),
    url(r'^nm$', 'chuangxing.views.nm', name='nm'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^xadmin/', include(xadmin.site.urls), name='xadmin'),
)
	