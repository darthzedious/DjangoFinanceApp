# Generated by Django 5.1.1 on 2024-11-28 11:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repayment_plans_app', '0006_alter_equalinstallmentplan_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EqualPrinciplePortion',
            new_name='EqualPrinciplePortionPlan',
        ),
    ]