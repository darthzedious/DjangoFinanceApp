from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

UserModel = get_user_model()

class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        user = None

        # Attempt to retrieve the user by email
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            # If no user by email, try getting the user by username
            try:
                user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                return None

        # Check password and user authentication status
        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user