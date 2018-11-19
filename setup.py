from db_config import create_tables
from app.views import UserView

create_tables()

print("Welcome to our program . Be awesome\n")

signed_up = input("Are you registered if yes enter y if not enter any word\n")

signed_up_lower = signed_up.lower()
user = UserView()

data = False
while data is not True:
    if signed_up_lower != "y":
        print("You will be required to sign-up\n")
        name = input("please enter your name\n")
        password = input("please enter your password\n")
        signup = user.sign_up(name, password)
        if not signup:
            print("User name exist change the user_name")
            data = False
        else:
            data = True
    else:
        data = True


print("Please you will be required to Enter your user_name and password\n")
user_name = input("Please provide us with your user name\n")
password = input("Please provide us with your password\n")
login = user.sign_in("name", "password")
while login is not True:
    print("oops sorry your password and user name combination is wrong")
    user_name = input("Please provide us with your user name\n")
    password = input("Please provide us with your password\n")
    login = user.sign_in("name", "password")














