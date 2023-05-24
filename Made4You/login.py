users = {
    'user1': {
        'password': 'password1',
        'role': 'admin'
    },
    'user2': {
        'password': 'password2',
        'role': 'guest'
    }
}

def login():
    username = input("Username: ")
    password = input("Password: ")

    if username in users and password == users[username]['password']:
        return users[username]['role']
    else:
        return None

def admin_actions():
    print("Performing admin actions...")
    # Add your admin-specific actions here

def guest_actions():
    print("Performing guest actions...")
    # Add your guest-specific actions here

def main():
    role = login()
    if role == 'admin':
        admin_actions()
    elif role == 'guest':
        guest_actions()
    else:
        print("Invalid username or password.")

if __name__ == "__main__":
    main()
