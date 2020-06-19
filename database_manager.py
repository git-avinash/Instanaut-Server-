import sqlite3


class account:
    def __init__(self):
        self.conn = sqlite3.connect('accounts.db')

        self.c = self.conn.cursor()

        with self.conn:
            self.c.execute(
                "CREATE TABLE IF NOT EXISTS accounts (username text, password text)")

    def create_user(self, username, password):
        with self.conn:
            self.c.execute("INSERT INTO accounts VALUES (:username, :password)", {
                           'username': username, 'password': password})

    def user_data(self, username):
        with self.conn:
            self.c.execute(
                "SELECT * FROM accounts WHERE username=:username", {'username': username})
            self.user_data = self.c.fetchall()
            return self.user_data

    def remove_user(self, username):
        with self.conn:
            self.c.execute("DELETE FROM accounts WHERE username=:username", {
                           'username': username})

    def all_data(self):
        with self.conn:
            self.c.execute("SELECT * FROM accounts")
            return self.c.fetchall()


class sessions:
    def __init__(self):
        self.conn = sqlite3.connect('sessions.db')

        self.c = self.conn.cursor()

        with self.conn:
            self.c.execute(
                "CREATE TABLE IF NOT EXISTS sessions (user text, key text, working_status integer,lk_status_hashtag integer, hashtag text, lk_status_comment integer, comments text, lk_status_location integer, url text, st_status_hashtag integer, st_status_location integer)")

    def create_session(self,
                       user,
                       key,
                       working_status,
                       lk_status_hashtag,
                       hashtag,
                       lk_status_comment,
                       comments,
                       lk_status_location,
                       url,
                       st_status_hashtag,
                       st_status_location,):
        with self.conn:
            self.c.execute("INSERT INTO sessions VALUES (:user, :key, :working_status,:lk_status_hashtag, :hashtag, :lk_status_comment, :comments, :lk_status_location, :url, :st_status_hashtag, :st_status_location)", {
                "user": user,
                "key": key,
                "working_status": working_status,
                "lk_status_hashtag": lk_status_hashtag,
                "hashtag": hashtag,
                "lk_status_comment": lk_status_comment,
                "comments": comments,
                "lk_status_location": lk_status_location,
                "url": url,
                "st_status_hashtag": st_status_hashtag,
                "st_status_location": st_status_location,
            })

    def delete_session(self, key):
        with self.conn:
            self.c.execute("DELETE FROM sessions WHERE key=:key", {"key": key})

    def all_sessions(self):
        with self.conn:
            self.c.execute("SELECT * FROM sessions")
            return self.c.fetchall()

    def session_data(self, user):
        with self.conn:
            self.c.execute(
                "SELECT * FROM sessions WHERE user=:user", {'user': user})
            self.user_data = self.c.fetchall()
            return self.user_data

    def update_run_status(self, session_key, working_status):
        with self.conn:
            self.c.execute("UPDATE sessions SET working_status=:working_status WHERE key=:key", {
                           "working_status": working_status, "key": session_key})

    def session_data_by_key(self, key):
        with self.conn:
            self.c.execute(
                "SELECT * FROM sessions WHERE key=:key", {'key': key})
            self.session_data = self.c.fetchall()
            return self.session_data


class key_logger:
    def __init__(self):
        self.conn = sqlite3.connect('keys.db')

        self.c = self.conn.cursor()

        with self.conn:
            self.c.execute(
                "CREATE TABLE IF NOT EXISTS keys (key text)")

    def store_key(self, key):
        with self.conn:
            self.c.execute("INSERT INTO keys VALUES (:key)", {"key": key})

    def all_keys(self):
        with self.conn:
            self.c.execute("SELECT * FROM keys")
            return self.c.fetchall()
