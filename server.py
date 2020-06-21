import socket
import json

from signup import SignUp
from database_manager import account, sessions
from interact import gen_key, convert_tf, get_list_from_string
from main import app
from run_sessions import session_runner

HEADERSIZE = 10
SERVER = "0.0.0.0"
PORT = 5050
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
COMMAND = 'command'
SUCCESS_CODE = {'status': 'success'}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)
s.listen(5)
print(f"[ACTIVE] Hosted on {SERVER}")
print(f"[CONNECT TO] {socket.gethostbyname(socket.gethostname())}")
print(f"[PORT] {PORT}")

run_session = session_runner()
# run_session.start_all_existing_sessions()


def send_msg(client_socket, send_message):
    final_send_message = json.dumps(send_message)
    client_socket.send(bytes(final_send_message, FORMAT))


while True:
    client_socket, address = s.accept()
    print(f"[CONNECTED] {address}")
    header = b''
    while len(header) < HEADERSIZE:
        chunk = client_socket.recv(HEADERSIZE - len(header))
        if chunk == b'':
            break
        header += chunk

    if len(header) < HEADERSIZE:
        print("Client disconnected without sending full header")
        continue

    payload_len = int(header)
    payload = b''
    while len(payload) < payload_len:
        chunk = client_socket.recv(payload_len - len(payload))
        if chunk == b'':
            break
        payload += chunk

    if len(payload) < payload_len:
        print("Client disconnected without sending full payload")
        continue

    payload = payload.decode(FORMAT)
    print(f"[REQUEST] {payload}")
    request = json.loads(payload)

    """xX COMMANDS BELOW Xx"""
    #
    if request[COMMAND] == "connectionTest":
        send_msg(client_socket, SUCCESS_CODE)

    if request[COMMAND] == "createAccount":
        username = request["username"]
        password = request["password"]

        instance = SignUp(username, password)
        message = instance.signup()

        db = account()
        db.create_user(username, password)

        send_message = {'status': message}
        send_msg(client_socket, send_message)
    #
    if request[COMMAND] == "createSession":
        working_status = request["working_status"]
        lk_status_hashtag = request["lk_status_hashtag"]
        hashtag = request["hashtag"]
        lk_status_comment = request["lk_status_comment"]
        comments = request["comments"]
        lk_status_location = request["lk_status_location"]
        url = request["url"]
        st_status_hashtag = request["st_status_hashtag"]
        st_status_location = request["st_status_location"]

        user_id = request["username"]

        key = gen_key()

        s_db = sessions()
        s_db.create_session(
            user_id,
            key,
            convert_tf(working_status),
            convert_tf(lk_status_hashtag),
            hashtag,
            convert_tf(lk_status_comment),
            str(comments),
            convert_tf(lk_status_location),
            url,
            convert_tf(st_status_hashtag),
            convert_tf(st_status_location),
        )
        run_session.start_single_session(user_id, key)

        send_msg(client_socket, SUCCESS_CODE)
    #
    if request[COMMAND] == "fetchAllUsers":
        db = account()
        all_data = db.all_data()

        user_data = []

        for data in all_data:
            user_data.append(data[0])

        message = {"user_data": user_data}

        send_msg(client_socket, message)
    #
    if request[COMMAND] == "fetchSessionData":
        user_id = request["username"]

        db = sessions()
        user_session_data = db.session_data(user_id)

        session_data = []

        for session in user_session_data:
            data = {
                # "user": session[0],
                "key": session[1],
                "working_status": session[2],
                "lk_status_hashtag": session[3],
                "hashtag": session[4],
                "lk_status_comment": session[5],
                "comments": get_list_from_string(session[6]),
                "lk_status_location": session[7],
                "url": session[8],
                "st_status_hashtag": session[9],
                "st_status_location": session[10],
            }
            session_data.append(data)
        message = {"data": session_data}
        send_msg(client_socket, message)
    #
    if request[COMMAND] == "triggerSessionActivity":
        user_id = request["username"]
        session_id = request["key"]
        working_status = request["working_status"]

        db = sessions()
        db.update_run_status(session_id, working_status)

        send_msg(client_socket, SUCCESS_CODE)

        if request["working_status"] == 1:
            run_session.start_single_session(user_id, session_id)

    if request[COMMAND] == "deleteAccount":
        user_id = request["username"]

        db = account()
        db.remove_user(user_id)

        send_msg(client_socket, SUCCESS_CODE)
    #
    if request[COMMAND] == "deleteSession":
        sessionKey = request["sessionKey"]

        db = sessions()
        db.delete_session(sessionKey)

        send_msg(client_socket, SUCCESS_CODE)

    if request[COMMAND] == "runAllSessions":
        pass

    if request[COMMAND] == "stopAllSessions":
        pass

    else:
        pass
