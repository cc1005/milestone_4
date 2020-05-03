from django.conf.urls import url, include
from .views import total_catalogue, access_full_documents

urlpatterns = [
    url(r'^$', total_catalogue, name="catalogue"),
    url(r'^fulldocument$', access_full_documents, name="fulldocument")
]