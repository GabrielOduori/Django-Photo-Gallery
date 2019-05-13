from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    # url(r'^$', views.welcome, name = 'welcome'),
    url(r'^$', views.index, name = 'home'),
    url(r'^gallery/$', views.gallery, name = 'gallery'),
    url(r'^gallery/<int:image_id>/$', views.single_image_details, name='image_details'),
    url(r'^about/$', views.about_us, name = 'about'),
    url(r'^search/$', views.search_images, name = 'search_images'),
    url(r'^category/sports/$', views.sports, name = 'sports'),
    url(r'^category/technology/$', views.technology, name = 'technology'),
    url(r'^category/nature/$', views.nature, name = 'nature'),
    url(r'^category/entertainment/$', views.entertainment, name = 'entertainment'),
    url(r'^admin/', admin.site.urls), name="admin",

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
