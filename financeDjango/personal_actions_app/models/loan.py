from django.contrib.auth import get_user_model
from django.db import models

from financeDjango.personal_actions_app.choices import LoanTypeChoices

UserModel = get_user_model()
class Loan(models.Model):

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='loans',
    )
    type = models.CharField(max_length=20, choices=LoanTypeChoices.choices)
    principal = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)  # Annual rate as %
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.type.capitalize()} Loan for {self.user.email}"