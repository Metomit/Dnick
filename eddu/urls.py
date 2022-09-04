from django.urls import path
from . import views

#URLconf
urlpatterns = [
    path('login', views.login_req),
    path('', views.login_req),
    path('select_course', views.actual_login),
    path('logout', views.logout),
    path('video', views.video),
    path('stream', views.stream),
]