from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('hashtags/<int:hashtag_id>/', views.hashtags, name='hashtags'),

    path('create/', views.create, name='create'),

    path('<int:post_id>/update/', views.update, name='update'),

    path('<int:post_id>/delete/', views.delete, name='delete'),

    path('<int:post_id>/like/', views.like, name='like'),

    path('search/', views.search, name='search'),
]
