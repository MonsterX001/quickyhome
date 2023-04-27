from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('account', views.account, name='account'),
    path('logout', views.logout, name='logout'),
    path('Houseupload', views.Houseupload, name='Houseupload'),
    path('search', views.search, name='search'),
    path('houses/<str:id>', views.houses, name='houses'),
]