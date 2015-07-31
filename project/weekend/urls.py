from django.conf.urls import url
from weekend.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
]
