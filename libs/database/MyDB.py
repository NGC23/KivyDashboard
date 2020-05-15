import sqlite3


class MyDB(object):
    DB_PATH = "dietPyApp.db"

    # Magic method, on class init it will assign these values
    def __init__(self) -> object:
        print("db instantiated")
        self.sql = sqlite3.connect(self.DB_PATH)
        self.sql_cur = self.sql.cursor()

    def query(self, query, params=[]) -> object:
        print("Executing", query)
        try:
            return self.sql_cur.execute(query, params)
        except sqlite3.Error as error:
            raise Exception("Error executing query", error)

    def commit(self):
        print("We are commititng changes")
        self.sql.commit()

    def fetch(self, query, params):
        print("Executing", query)
        try:
            result = self.sql_cur.execute(query, params)
            return result.fetchall()
        except sqlite3.Error as error:
            raise Exception("Error executing fetch query", error)

    # On class destruction we close the DB
    def __del__(self):
        print("close db")
        self.sql.close()
