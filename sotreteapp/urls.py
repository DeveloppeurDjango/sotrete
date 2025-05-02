from django.urls import path
from .views import home, about, service, contact, confirmation, search, detail, gallery
from django.conf import settings


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('gallery/', gallery, name='gallery'),
    path('contact/', contact, name='contact'),
    path('confirmation/', confirmation, name='confirmation'),
    path('article/<int:id_article>/', detail, name="detail"),
    path('article/recherche/', search, name="search"),
]

