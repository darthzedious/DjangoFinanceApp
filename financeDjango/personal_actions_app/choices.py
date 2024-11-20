from django.db import models


class TransactionTypes(models.TextChoices):
    INCOME = 'Income', 'Income'
    EXPENSE = 'Expense', 'Expense'


class LoanTypeChoices(models.TextChoices):
    PERSONAL = 'Personal', 'Personal'
    MORTGAGE = 'Mortgage', 'Mortgage'
    AUTO = 'Auto', 'Auto'
    EDUCATION = 'Education', 'Education'
