from django.urls import path
from .views import home, about, service, contact, confirmation, search, detail, gallery
from django.conf import settings
from django.conf.urls.static import static  # Ajoutez cette importation
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('gallery/', gallery, name='gallery'),
    path('contact/', contact, name='contact'),
    path('confirmation/', confirmation, name='confirmation'),
    path('article/<int:id_article>/', detail, name="detail"),
    path('article/recherche/', search, name="search"),
        path('google439126b94a9dcf8a.html', serve, {'document_root': 'sotreteapp/templates', 'path': 'google439126b94a9dcf8a.html'}),
    path('sitemap.xml', serve, {'document_root': '', 'path': 'sitemap.xml'}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()