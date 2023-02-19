from django.urls import include, path
from crud import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='index'),
    path('create/', views.create, name='create'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('edit_user', views.edit_user, name='edit_user'),
    path('order_list', views.orders, name='orders'),
    path('login', views.logform, name='logform'),
    path('login/', views.login, name='login'),
    path('register', views.register, name='register'),
    path('check_login/', views.check_login, name='check_login'),
    path('check_email/', views.check_email, name='check_email'),
    path('check_password/', views.check_passwordlen, name='check_password'),
    path('logout', views.logout, name='logout'),

]
