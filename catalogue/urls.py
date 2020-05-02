from django.conf.urls import url, include
from .views import total_catalogue

urlpatterns = [
    url(r'^$', total_catalogue, name="catalogue")
]