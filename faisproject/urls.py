from django.contrib import admin
from django.urls import path
from tokobunga import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('about/',views.about),
    path('gifts/',views.gifts),
    path('shop/',views.shop),
    path('contact/',views.contact),
]
