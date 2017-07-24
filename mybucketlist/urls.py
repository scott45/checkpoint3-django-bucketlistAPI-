from django.conf.urls import url, include
from django.contrib import admin
from apiv2 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(
        r'^api/v1/bucketlists/(?P<pk>[0-9]+)$', views.get_delete_update_bucketlist,
        name='get_delete_update_bucketlist'),
    url(r'^api/v1/bucketlists/$', views.get_post_bucketlist, name='get_post_bucketlists')
]
