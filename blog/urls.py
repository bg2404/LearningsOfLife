from django.urls import re_path, include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog'

urlpatterns = [
    re_path('^$', views.BlogList.as_view(), name='index'),
    re_path('^author/$', views.AuthorView.as_view(), name='author'),
    re_path('^blog/(?P<slug>[\w-]+)/$', views.blog_detail, name='blog_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_DIR)
