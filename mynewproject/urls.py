from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from mynewproject import settings
from home.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mynewproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',home),
    url(r'^home/$',home),
    url(r'^contact/$',contact), 
    url(r'^aboutus/$',aboutus),    
    url(r'^faqs/$',faqs),
    url(r'^benefits/$',benefits), 
    url(r'^technology/$',technology),
    url(r'^project/$',project),
    
    
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
