from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from news.views import index, news, category, gallery, article, search, article_create, article_update, article_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', index, name='index'),
    path('news/', news, name='news'),
    path('news/<str:category>/', category, name='category'),
    path('gallery/', gallery, name='gallery'),
    path('search/', search, name='search'),
    path('create/', article_create, name='create'),
    path('article/<id>/update/', article_update, name='article_update'),
    path('article/<id>/delete/', article_delete, name='article_delete'),
    path('article/<id>/', article, name='article'),
    path('accounts/', include('allauth.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
