from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'smu5.views.main', name='main'),
    url(r'^admin/', include(admin.site.urls)),
]
