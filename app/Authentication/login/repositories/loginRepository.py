import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv
from pathlib import Path
from app.Authentication.models.User import User
from libs.database.MyDB import MyDB


class LoginRepository(object):

    def __init__(self) -> object:
        env_path = Path('.') / '.env'
        load_dotenv(dotenv_path=env_path)

    @property
    def __sql(self):
        # Need to see cleaner way of implementation - for now it is a private class property
        return MyDB()

    def login_user(self, username: str, password: str) -> User:
        try:
            result = self.__sql.fetch("SELECT * FROM user_details WHERE username = ?", [username])
            print(result[0])
            # Create user object from the result, we will return this to the controller and screen and pass
            # user.password to the function in refactor
            if self.__check_password(password, result[0][1]):
                return User(result[0][0], result[0][1], result[0][2])
        except RuntimeError:
            raise Exception("Issue retuning user in repository")
        pass

    def __check_password(self, password: str, retrieved_password: str) -> bool:
        key = os.environ.get('PASSWORD_KEY')
        cipher_suite = Fernet(key)

        if password.encode() == cipher_suite.decrypt(retrieved_password):
            return True

        return False
