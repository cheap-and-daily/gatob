from django.db import models
from django.contrib.auth.models import User


class Subscription(models.Model):
    PLAN_CHOICES = [
        ('monthly', 'Месячный план'),
        ('three_month', 'Трехмесячный план'),
        ('yearly', 'Годовой план'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    visits = models.PositiveIntegerField(blank=True)
    priority_booking = models.BooleanField(default=True)
    ticket_discount = models.BooleanField(default=True)
    exclusive_events = models.BooleanField(default=True)
    gifts_and_bonuses = models.BooleanField(default=True)
    unlimited_visits = models.BooleanField(default=False)
    special_certificate = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Subscription"
