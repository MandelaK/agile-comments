from db_config import create_tables
from app.views import UserView

create_tables()

print("Welcome to our program . Be awesome\n")

signed_up = input("Are you registered if yes enter y if not enter any word\n")

signed_up_lower = signed_up.lower()

data = False
while data is not True:
    if signed_up_lower != "y":
        print("You will be required to sign-up\n")
        name = input("please enter your name\n")
        password = input("please enter your password\n")
        user = UserView()
        signup = user.UserView(name, password)
        if not signup:
            print("User name exist change the user_name")
            data = False
        else:
            data = True
    else:
        pass
print("Please Enter your user_name and password")











