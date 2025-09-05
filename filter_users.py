import json

USERS_FILE_PATH = 'users.json'

def load_data(file_path):
    """Load user data from JSON file."""
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
    """
        Filter users by name and print the results.
    """
    filtered_users = filter_users(users,'name',name)
    print_results(filtered_users)

def filter_users_by_age(age,users):
    """
       Filter users by age and print the results.
    """
    filtered_users = filter_users(users,'age',age)
    print_results(filtered_users)

def filter_users_by_email(email,users):
    """
       Filter users by email and print the results.
    """
    filtered_users = filter_users(users,'email',email)
    print_results(filtered_users)

def print_results(results: list[dict]):
    """Print filtered users or a message if none found."""
    if not results:
        print("No users found.")
    else:
        for user in results:
            print(user)

if __name__ == "__main__":
    users = load_data(USERS_FILE_PATH)
    filter_option = input("What would you like to filter by? ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search,users)
    elif filter_option =='age':
        age_input = input("Enter an age to filter users: ").strip()
        if age_input.isdigit():
            filter_users_by_age(int(age_input), users)
        else:
            print("Invalid input: age must be a number.")
    elif filter_option == 'email':
        email_to_search = input('Enter an email to filter users:')
        filter_users_by_email(email_to_search,users)
    else:
        print("Filtering by that option is not yet supported.")