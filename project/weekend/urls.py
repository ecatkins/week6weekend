from django.conf.urls import url
from weekend.views import IndexView, InstagramView, FrontView, GayPrideView, WWCView
urlpatterns = [
    url(r'^$', FrontView.as_view(),name='front'),
    url(r'^gay_pride$', IndexView.as_view(), name='gay_pride_index'),
    url(r'^gay_pride/info$', GayPrideView.as_view(), name='gay_pride_info'),
     url(r'^wwc$', IndexView.as_view(), name='wwc_index'),
    url(r'^wwc/info$', WWCView.as_view(), name='wwc_info'),
    url(r'^instagram/(?P<event_name>[\w]*)/(?P<search>[\w]*)/(?P<interval>[\w]*)$', InstagramView.as_view(), name='instagram'),
    url(r'^flag$', 'weekend.views.flag', name='flag'),
    url(r'^soccer$', 'weekend.views.soccer', name='soccer'),
]
