from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Budget(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='budget',
    )

    category = models.CharField(
        max_length=50,
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.amount} for period {self.start_date} to {self.end_date}"
