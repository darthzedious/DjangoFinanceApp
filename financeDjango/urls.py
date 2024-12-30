"""
URL configuration for financeDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import financeDjango
from financeDjango import shares_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('financeDjango.home_menu_app.urls')),
    path('shares/', include('financeDjango.shares_app.urls')),
    path('accounts/', include('financeDjango.accounts.urls')),
    path('future-value/', include('financeDjango.future_value_app.urls')),
    path('discount-factor/', include('financeDjango.discount_factor_app.urls')),
    path('personal-actions/', include('financeDjango.personal_actions_app.urls')),
    path('repayment_plans/', include('financeDjango.repayment_plans_app.urls')),
    path('annuity_factor/', include('financeDjango.annuity_factor_app.urls')),
]
