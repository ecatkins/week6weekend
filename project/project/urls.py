from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^instavent/', include('weekend.urls', namespace='instavent')),
    url(r'^admin/', include(admin.site.urls)),
]
