from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.index, name='index'),
    path('hashtags/<int:hashtag_id>/', views.hashtags, name='hashtags'),

    path('search/', views.search, name='search'),

    path('create/', views.create, name='create'),
    path('<int:post_id>/update/', views.update, name='update'),
    path('<int:post_id>/delete/', views.delete, name='delete'),

    path('<int:post_id>/comment/create/',
         views.comment_create, name='comment_create'),
    path('<int:post_id>/comment/<int:comment_id>/delete/',
         views.comment_delete, name='comment_delete'),

    path('<int:post_id>/like/', views.like, name='like'),
]
