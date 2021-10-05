from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('signup/', views.signup, name='signup'),

    path('update/', views.update, name='update'),
    path('password/', views.password, name='password'),

    path('<int:user_id>/delete/', views.delete, name='delete'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('<int:user_id>/', views.userpage, name='userpage'),
    path('profile/', views.profile, name='profile'),
    path('<int:user_id>/follow/', views.follow, name='follow'),
]
