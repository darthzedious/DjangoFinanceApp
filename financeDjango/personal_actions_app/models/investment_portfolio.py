from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

class InvestmentPortfolio(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='investment_portfolio',
    )

    name = models.CharField(
        max_length=100,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.name}"