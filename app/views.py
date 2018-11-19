"""Docstring for views."""
from .models import UserModel


class UserView():
    """This view handles requests for user actions."""

    def __init__(self):
        """Docstring for init method."""
        self.user = UserModel()

    def sign_up(self, user_name, password):
        submit_sign_up = self.user.sign_up_model(user_name, password)

        if not submit_sign_up:
            return False

        else:
            return True

    def sign_in(self, user_name, password):
        submit_login = self.user.sign_in_model(user_name, password)

        if submit_login == 404:
            return "user does not exist"
        else:
            return True
