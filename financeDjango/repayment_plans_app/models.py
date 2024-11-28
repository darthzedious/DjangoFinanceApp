from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

UserModel = get_user_model()


class BaseEqualCPPPlan(models.Model):
    class Meta:
        abstract = True

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='%(class)s_plans',
    )

    borrowed_amount = models.FloatField(
        validators=[
            MinValueValidator(0.01),
        ],
        null=False,
        blank=False,
    )

    interest_rate = models.FloatField(
        validators=[
            MinValueValidator(0.01),
            MaxValueValidator(1.0),
        ],
        null=False,
        blank=False,
    )

    periods = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
        ],
        null=False,
        blank=False,
    )

    repayment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    def __str__(self):
        return f"Repayment Plan for {self.user} - {self.borrowed_amount}"


class EqualInstallmentPlan(BaseEqualCPPPlan):
    pass


class EqualPrincipalPortionPlan(BaseEqualCPPPlan):
    pass


class BaseChangeableIPPlan(models.Model):
    class Meta:
        abstract = True

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='%(class)s_plans',
    )

    borrowed_amount = models.FloatField(
        validators=[
            MinValueValidator(0.01),
        ],
        null=False,
        blank=False,
    )

    interest_rate_first_period = models.FloatField(
        validators=[
            MinValueValidator(0.01),
            MaxValueValidator(1.0),
        ],
        null=False,
        blank=False,
    )

    interest_rate_second_period = models.FloatField(
        validators=[
            MinValueValidator(0.01),
            MaxValueValidator(1.0),
        ],
        null=False,
        blank=False,
    )

    first_period = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
        ],
        null=False,
        blank=False,
    )

    second_period = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
        ],
        null=False,
        blank=False,
    )

    repayment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    def __str__(self):
        return f"Repayment Plan for {self.user} - {self.borrowed_amount}"


class EqualInstallmentChangeableIPPlan(BaseChangeableIPPlan):
    pass

class EqualPrincipalPortionChangeableIPPlan(BaseChangeableIPPlan):
    pass