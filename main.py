from Instanaut import Instanaut


class app:
    def __init__(self,
                 key,
                 username,
                 password,
                 lk_status_hashtag,
                 hashtag,
                 lk_status_comment,
                 comments,
                 lk_status_location,
                 url,
                 st_status_hashtag,
                 st_status_location,
                 ):

        self.user_session = Instanaut(username, password)
        self.user_session.session(key,
                                  lk_status_hashtag,
                                  hashtag,
                                  lk_status_comment,
                                  comments,
                                  lk_status_location,
                                  url,
                                  st_status_hashtag,
                                  st_status_location,
                                  )
