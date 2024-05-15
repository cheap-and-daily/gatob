from django.urls import path
from .views import news_feed, add_comment, pricing
from plays.views import performances_list

urlpatterns = [
    path('', performances_list, name='news_feed'),
    path('add_comment/<int:news_id>/', add_comment, name='add_comment'),
    path('subscriptions', pricing, name='pricing')
]
