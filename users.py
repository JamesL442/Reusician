#users dictionary
users = {
    "testuser": "testpass"
}

def append_user(username, password):
    users[username] = password

def get_user(username):
    return users.get(username)

def update_user(old_username, new_username, new_password):
    if old_username in users:
        del users[old_username]  # Ensure the old username is deleted
        users[new_username] = new_password