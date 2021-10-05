from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('update/', views.update, name='update'),
    path('password/', views.password, name='password'),
    path('<int:user_id>/delete/', views.delete, name='delete'),

    path('<int:user_id>/', views.userpage, name='userpage'),
    path('<int:user_id>/follow/', views.follow, name='follow'),
]
