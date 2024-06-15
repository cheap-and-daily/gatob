from django.urls import path
from .views import news_feed, add_comment, delete_comment, pricing, payment, credit_card_payment, admin_payment, interview_view
from plays.views import performances_list

urlpatterns = [
    path('', performances_list, name='afisha'),
    path('news/', news_feed, name='news_feed'),
    path('add_comment/<int:news_id>/', add_comment, name='add_comment'),
    path('delete_comment/<int:comment_id>/', delete_comment, name='delete_comment'),
    path('subscriptions', pricing, name='pricing'),
    path('payment/', payment, name='payment'),
    path('payment/credit-card/', credit_card_payment, name='credit_card_payment'),
    path('payment/admin-payment/', admin_payment, name='admin_payment'),
    path('interview/', interview_view, name='interview'),
]
