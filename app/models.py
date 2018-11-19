"""Docstring for models."""
from db_config import init_db


class UserModel():
    """docstring for UserModel."""

    def __init__(self):
        """Docstring for init method."""
        self.connection = init_db()

    def sign_up_model(self, username, password):
        """Docstring for sign_up method."""
        payload = {
            "role": "user",
            "username": username,
            "password": password
        }
        query = """INSERT INTO users (user_name,password,role)
        VALUES (%(username)s,%(password)s,%(role)s);"""
        try:
            cur = self.connection.cursor()
            cur.execute(query, payload)
            self.connection.commit()
            return True
        except:
            return False

    def get_user_by_name(self, username):
        """Docstring for get username."""
        cur = self.connection.cursor()
        cur.execute(
            """SELECT * FROM users WHERE user_name = %s ;""", (username,))
        one = cur.fetchone()
        return one

    def sign_in_model(self, username, password):
        """Docstring for sign_in method."""
        user = self.get_user_by_name(username)

        if not user:
            return 404
        uname = user[1]
        pwd = user[2]

        if uname == username and pwd == password:
            return user
        else:
            return False

