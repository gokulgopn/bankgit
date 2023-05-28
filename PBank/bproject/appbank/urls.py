from django.urls import path
from appbank import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('loginn/',views.loginn,name='loginn'),
    path('new/',views.new,name='new'),
    path('form/',views.form,name='form'),
    path('final',views.final,name='final'),
    path('redirect_idukki',views.redirect_idukki,name='redirect_idukki'),
    path('redirect_kottayam',views.redirect_kottayam,name='redirect_kottayam'),
    path('redirect_malappuram',views.redirect_malappuram,name='redirect_malappuram'),
    path('redirect_palakkad',views.redirect_palakkad,name='redirect_palakkad'),
    path('redirect_kochi',views.redirect_kochi,name='redirect_kochi'),


]
