from django.urls import path , re_path
from django.contrib import admin

from boards import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^admin/', admin.site.urls),
]
