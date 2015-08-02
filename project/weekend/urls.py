from django.conf.urls import url
from weekend.views import IndexView, InstagramView, FrontView, GayPrideView
urlpatterns = [
    url(r'^$', FrontView.as_view(),name='front'),
    url(r'^gay_pride$', IndexView.as_view(), name='gay_pride_index'),
    url(r'^gay_pride/info$', GayPrideView.as_view(), name='gay_pride_info'),
    url(r'^instagram/(?P<event_name>[\w]*)/(?P<search>[\w]*)/(?P<interval>[\w]*)$', InstagramView.as_view(), name='instagram'),
    url(r'^flag$', 'weekend.views.flag', name='flag'),
]
