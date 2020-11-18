from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from blog import urls as blog_urls
from organizer import urls as organizer_urls
from django.conf import settings
from django.contrib.auth import login

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(organizer_urls)),
    url(r'^blog/', include(blog_urls)),
    path('accounts/', include('allauth.urls')),
    path('api/', include('api.urls'))
]
