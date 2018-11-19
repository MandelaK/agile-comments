from models import UserModel


class UserView(UserModel):
    """This view handles requests for user actions"""

    def sign_up(self, user_name, password):
        submit_sign_up = self.user.sign_up(user_name, password)

        if not submit_sign_up:
            return "Error. Could not sign you up."

        else:
            return "Successfully signed you in."
