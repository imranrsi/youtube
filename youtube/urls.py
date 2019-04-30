from youtube import views
from django.urls import path

app_name='youtube'
urlpatterns = [
    path('index/', views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('other/',views.other,name='other'),

]
