current_users = ['user1', 'User2', 'user3', 'user4', 'User5']
current_users_lower = [user.lower() for user in current_users]
new_users = ['User3', 'user6', 'user5', 'user8', 'user9']

for user in new_users:
    if user.lower() in current_users_lower:
        print(
            f"The username {user} has already been taken. Please enter a new username.")
    else:
        print(f"Username {user} is available.")
