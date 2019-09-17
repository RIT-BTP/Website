from models import *


def user_check(username):
    known_users = tmpUsers.get()
    if username in [user.name for user in known_users]:
        return True
    else:
        return False
