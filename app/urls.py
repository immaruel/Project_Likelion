from django.urls import path
from . import views
from .decorators import unauthenticated_user, allowed_users, admin_only

urlpatterns = [
    path('', views.home, name="home"),
    path('product/', views.product, name="product"),
    path('customer/<str:pk_test>/', views.customer,name="customer"),
    path('user/', views.userPage, name="user"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user/', views.userPage, name="user"),
    path('adminpage/', views.adminDashboard, name="adminpage"),
    path('create/', views.createOrder, name="create"),
    path('delete/<int:pk>', views.deleteOrder, name="delete"),
    path('update/<int:pk>', views.updateOrder, name="update"),
    path('book/', views.bookPhoto, name="book"),
    path('book/', views.bookTitle, name="book"),
    path('book/', views.bookWriter, name="book"),
    path('book/', views.bookPublisher, name="book"),




    

]