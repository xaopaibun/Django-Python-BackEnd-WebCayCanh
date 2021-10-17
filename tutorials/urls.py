from django.conf.urls import url
from tutorials import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^department$',views.departmentApi),
    url(r'^department/([0-9]+)$',views.departmentApi),
    url(r'^productstree$',views.productsTreesApi),
    url(r'^productstree/([0-9]+)$',views.productsTreesApi),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)