from django.conf.urls import url, include


urlpatterns = [
    url(r'^$', all_products, name="products")
]