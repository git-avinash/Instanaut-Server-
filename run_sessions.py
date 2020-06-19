from database_manager import sessions, account
from main import app
from interact import convert_tf, get_list_from_string


def get_credentials(username):
    users = account()
    try:
        all_acc = users.all_data()
    except Exception as e:
        print(e)
        all_acc = None
    for acc in all_acc:
        if acc[0] == username:
            return acc[0], acc[1]


class session_runner:
    def __init__(self):
        self.db = sessions()
        self.all_sessions = self.db.all_sessions()

    def start_single_session(self, user_id, key):
        username = user_id
        user_id, password = get_credentials(username)

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

        app(
            user_id,
            password,
            lk_status_hashtag,
            hashtag,
            lk_status_comment,
            comments,
            lk_status_location,
            url,
            st_status_hashtag,
            st_status_location,
        )

    def start_all_existing_sessions(self):
        try:
            for session in self.all_sessions:
                if session[2] == "2":
                    username = session[0]
                    user_id, password = get_credentials(username)
                    lk_status_hashtag = convert_tf(session[3])
                    hashtag = session[4]
                    lk_status_comment = convert_tf(session[5])
                    comments = get_list_from_string(session[6])
                    lk_status_location = convert_tf(session[7])
                    url = session[8]
                    st_status_hashtag = convert_tf(session[9])
                    st_status_location = convert_tf(session[10])

                    app(
                        user_id,
                        password,
                        lk_status_hashtag,
                        hashtag,
                        lk_status_comment,
                        comments,
                        lk_status_location,
                        url,
                        st_status_hashtag,
                        st_status_location,
                    )
        except Exception as e:
            print(e)
