# I need to figure out the metaClasses and interfacing properly and how to correctly implement this
from libs.database.MyDB import MyDB
from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv
from pathlib import Path


class RegisterRepository(object):

    def __init__(self) -> object:
        print("prepping RegisterRepository.......")
        super(RegisterRepository, self).__init__()
        env_path = Path('.') / '.env'
        load_dotenv(dotenv_path=env_path)

    @property
    def __sql(self):
        return MyDB()

    def register_user(self, username: str, password: str, email: str) -> bool:
        key = os.environ.get('PASSWORD_KEY')
        print("Key from env file", key)
        cipher_suite = Fernet(key)
        ciphered_text = cipher_suite.encrypt(password.encode())
        print("password encrypted", ciphered_text)

        try:
            self.__sql.query("INSERT INTO user_details VALUES (?,?,?)", [username, ciphered_text, email])
            self.__sql.commit()
        except RuntimeError:
            return False

        return True
