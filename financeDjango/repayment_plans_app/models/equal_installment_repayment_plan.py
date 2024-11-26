from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

class EqualInstallmentPlan(models.Model):

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='equal_installment_plan',
    )

    borrowed_amount = models.FloatField()

    interest_rate = models.FloatField()

    periods = models.IntegerField()

    repayment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"Repayment Plan for {self.user} - {self.borrowed_amount}"