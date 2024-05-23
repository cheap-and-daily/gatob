from django.urls import path
from . import views

urlpatterns = [
    path('play/<int:play_id>/', views.play_detail, name='play_detail'),
    path('play/create/', views.play_create, name='play_create'),
    path('play/<int:play_id>/edit/', views.play_edit, name='play_edit'),
    path('actor/<int:actor_id>/', views.actor_detail, name='actor_detail'),
    path('actor/create/', views.actor_create, name='actor_create'),
    path('actor/<int:actor_id>/edit/', views.actor_edit, name='actor_edit'),
]
