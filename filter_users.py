import json

USERS_FILE_PATH = 'users.json'

def load_data(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def filter_users(users, key, value):
    """Generic user filter by key and value."""
    if key == "name":
        return [user for user in users if user.get("name", "").lower() == value.lower()]
    return [user for user in users if user.get(key) == value]

def filter_users_by_name(name,users):
    filtered_users = filter_users(users,'name',name)
    for user in filtered_users:
        print(user)

def filter_user_by_age(age,users):
    filtered_users = filter_users(users,'age',age)
    for user in filtered_users:
        print(user)

def filter_user_by_email(email,users):
    filtered_users = filter_users(users,'email',email)
    for user in filtered_users:
        print(user)

if __name__ == "__main__":
    users = load_data(USERS_FILE_PATH)
    filter_option = input("What would you like to filter by? ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search,users)
    elif filter_option =='age':
        age_to_search = int(input('Enter an age to filter users:'))
        filter_user_by_age(age_to_search,users)
    elif filter_option == 'email':
        email_to_search = input('Enter an email to filter users:')
        filter_user_by_email(email_to_search,users)
    else:
        print("Filtering by that option is not yet supported.")