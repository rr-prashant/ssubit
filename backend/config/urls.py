
from django.contrib import admin
from django.urls import include, path
from config.backapp1 import views


urlpatterns = [
    path("", views.hello),
    path('users/', views.UserView),
    path('groups/', views.GroupView),
    path('admin/', admin.site.urls),
]
