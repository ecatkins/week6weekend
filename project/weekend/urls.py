from django.conf.urls import url
from weekend.views import IndexView, InstagramView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^instagram$', InstagramView.as_view(), name='instagram'),
]
