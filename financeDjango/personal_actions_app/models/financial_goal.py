from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

class FinancialGoal(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='goals',
    )
    title = models.CharField(
        max_length=100,
    )

    target_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    saved_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    deadline = models.DateField()

    def __str__(self):
        return f"{self.title}: {self.saved_amount}/{self.target_amount}"