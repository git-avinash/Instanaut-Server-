import threading
import time

from database_manager import sessions, account
from main import app
from interact import convert_tf, get_list_from_string
from trigger_engine_activity import TriggerEngineActivity

thread_dict = {}


class session_runner:
    def __init__(self):
        self.db = sessions()
        self.all_sessions = self.db.all_sessions()

    def start_single_session(self, user_id, key):
        account_db = account()
        credentials = account_db.user_data(user_id)[0]
        user_id, password = credentials[0], credentials[1]

        session_data = self.db.session_data_by_key(key)[0]
        print(session_data)

        lk_status_hashtag = convert_tf(session_data[3])
        hashtag = session_data[4]
        lk_status_comment = convert_tf(session_data[5])
        comments = get_list_from_string(session_data[6])
        lk_status_location = convert_tf(session_data[7])
        url = session_data[8]
        st_status_hashtag = convert_tf(session_data[9])
        st_status_location = convert_tf(session_data[10])

        thread_dict[key] = threading.Thread(target=app, args=(user_id,
                                                              password,
                                                              lk_status_hashtag,
                                                              hashtag,
                                                              lk_status_comment,
                                                              comments,
                                                              lk_status_location,
                                                              url,
                                                              st_status_hashtag,
                                                              st_status_location))

        thread_dict[key].start()

    def start_all_existing_sessions(self):
        try:
            for session in self.all_sessions:
                if session[2] == 1:
                    username = session[0]
                    key = session[1]

                    account_db = account()
                    credentials = account_db.user_data(username)[0]
                    user_id, password = credentials[0], credentials[1]

                    lk_status_hashtag = convert_tf(session[3])
                    hashtag = session[4]
                    lk_status_comment = convert_tf(session[5])
                    comments = get_list_from_string(session[6])
                    lk_status_location = convert_tf(session[7])
                    url = session[8]
                    st_status_hashtag = convert_tf(session[9])
                    st_status_location = convert_tf(session[10])

                    thread_dict[key] = threading.Thread(target=app, args=(user_id,
                                                                          password,
                                                                          lk_status_hashtag,
                                                                          hashtag,
                                                                          lk_status_comment,
                                                                          comments,
                                                                          lk_status_location,
                                                                          url,
                                                                          st_status_hashtag,
                                                                          st_status_location))
                    thread_dict[key].start()
                    time.sleep(30)
        except Exception as e:
            print(e)

    def return_sessions_object_by_key(self, key):
        return thread_dict[key]

    def change_running_status(self, status):
        TriggerEngineActivity(is_running=status)
