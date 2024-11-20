from django.contrib.auth import  login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView

from financeDjango.accounts.forms import RegisterForm, ProfileEditForm, LoginForm
from financeDjango.accounts.models import Profile
from financeDjango.personal_actions_app.models import FinancialGoal, Budget

UserModel = get_user_model()

# def login_view(request):
#     if request.method == "POST":
#         form = LoginForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('profile')  # redirect to homepage after successful login
#             else:
#                 messages.error(request, "Invalid username or password")
#     else:
#         form = LoginForm()
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'accounts_templates/log_in.html', context)

class UserLoginView(LoginView):
    template_name = 'accounts_templates/log_in.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse('profile-details', kwargs={'pk': self.request.user.pk})

# def register_view(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('profile')  # redirect to homepage after successful registration
#     else:
#         form = RegisterForm()
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'accounts_templates/register.html', context)

class UserRegisterView(CreateView):
    model = UserModel
    form_class = RegisterForm
    template_name = 'accounts_templates/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object, backend='financeDjango.accounts.authentication.EmailOrUsernameBackend')

        return response

def logout_view(request):
    logout(request)
    return redirect('login')


class LoadProfile(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'accounts_templates/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['biggest_goal'] = (FinancialGoal.objects.filter(user=self.request.user)
                                   .order_by('-target_amount', '-deadline').first())
        context['latest_budget'] = Budget.objects.filter(user=self.request.user).order_by('start_date').first()
        return context

class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts_templates/profile-edit.html'

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == profile.user

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={
                'pk': self.object.pk,
            }
        )
