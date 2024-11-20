from django.contrib.auth import get_user_model
from django.db import models
from financeDjango.personal_actions_app.choices import TransactionTypes

UserModel = get_user_model()


class Transaction(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='transactions',
    )

    type = models.CharField(
        max_length=7,
        choices=TransactionTypes.choices,
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    date = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.type.capitalize()} of {self.amount} by {self.description}"