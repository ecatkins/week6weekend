from django.conf.urls import url
from weekend.views import IndexView, InstagramView, FrontView
urlpatterns = [
    url(r'^$', FrontView.as_view(),name='front')
    url(r'^gay_pride$', IndexView.as_view(), name='index'),
    url(r'^instagram/(?P<search>[\w]*)/(?P<interval>[\w]*)$', InstagramView.as_view(), name='instagram'),
    url(r'^flag$', 'weekend.views.flag', name='flag'),
]
