from django.conf.urls import url
from weekend.views import IndexView, InstagramView, FrontView
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^instagram$', InstagramView.as_view(), name='instagram'),
    url(r'^flag$', 'weekend.views.flag', name='flag'),
    url(r'^front$', FrontView.as_view(),name='front')
]
