from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^weekend/', include('weekend.urls', namespace='weekend')),
    url(r'^admin/', include(admin.site.urls)),
]
