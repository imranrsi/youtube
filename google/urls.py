from google import views
from django.urls import path
urlpatterns = [
    path('', views.home,name='home'),
    path('url/',views.url_info,name='url'),
    path('info/',views.user_info,name='info'),
    path('form/',views.formtest,name='form'),
]
