from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.home, name="home"),
    path('additem', views.additem, name='additem'),
    path('shoes', views.shoes, name='shoes'),
    path('blazers', views.blazers, name='blazers'),
    path('dresses', views.dresses, name='dresses'),
    path('gym', views.gym, name='gym'),
    path('jackets', views.jackets, name='jackets'),
    path('jeans', views.jeans, name='jeans'),
    path('makeup', views.makeup, name='makeup'),
    path('other', views.other, name='other'),
    path('shirts', views.shirts, name='shirts'),
    path('update/<itemid>', views.update, name="update"),
    path('delete/<itemid>', views.delete, name='delete'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register, name='register'),
    path('search', views.search, name='search'),
    path('chat', views.chat, name='chat'),
    path('order/<itemid>', views.order, name='order'),
    path('view/<itemid>', views.view_item, name='view'),
    path('dele/<cartid>', views.dele,name='dele'),
    path('cart', views.cart, name='cart')
]