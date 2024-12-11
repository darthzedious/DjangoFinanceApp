from django.urls import path
from django.urls.conf import include

from financeDjango.accounts import views

urlpatterns = [

    path('register/', views.UserRegisterView.as_view(), name='register'),

    path('login/', views.UserLoginView.as_view(), name='login'),

    path('logout/', views.logout_view, name='logout'),

    path('profile/<int:pk>/', include([
        path('', views.LoadProfile.as_view(), name='profile-details'),
        path('edit/', views.ProfileEditView.as_view(), name='profile-edit'),
    ]))
]