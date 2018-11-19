"""Docstring for models."""
from db_config import init_db


class UserModel(object):
    """docstring for UserModel."""

    def __init__(self):
        """Docstring for init method."""
        self.connection = init_db()

    def sign_up(self, **kwargs):
        """Docstring for sign_up method."""
        payload = {
            "role": "user",
            "username": kwargs["username"],
            "password": kwargs["password"]
        }
        query = """INSERT INTO users (user_name,password,role)
        VALUES (%s,%s,%s);""",
        (payload['username'], payload['password'], payload['role'])
        try:
            cur = self.connection.cursor()
            cur.execute(query)
            cur.commit()
        except Exception as e:
            raise e
