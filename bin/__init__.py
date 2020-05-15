from libs.database.MyDB import MyDB


class PrepApplicationInstall(object):
    def __init__(self):
        self.build_app_sql_tables()

    @property
    def __sql(self):
        # Need to see cleaner way of implementation
        return MyDB()

    def build_app_sql_tables(self):
        print("starting app sql build")
        self.__build_user_table()
        self.__build_food_diary_table()
        return

    def __build_user_table(self):
        try:
            print("creating users table...")
            self.__sql.query('''CREATE TABLE IF NOT EXISTS user_details(
                                    username TEXT(155),
                                    password TEXT(255),
                                    email TEXT(155)
                                )''', '')
            self.__sql.commit()
        except RuntimeError as error:
            print("Issue creating table", error)

        print("user table completed")
        return

    def __build_food_diary_table(self):
        try:
            print("creating food diary table")
            self.__sql.query('''CREATE TABLE IF NOT EXISTS food_diary(
                                    name TEXT(155),
                                    description TEXT(255),
                                    protein FLOAT,
                                    fats FLOAT,
                                    calories FLOAT,
                                    carbs FLOAT,
                                    serving_size FLOAT,
                                    measure FLOAT,
                                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                                )''', '')
            self.__sql.commit()
        except RuntimeError as error:
            print("Issue creating table", error)

        print("food diary table completed")
        return
