from src.followers import get_users_common_followers


def ask_usernames():
    first_username = input("Enter first username: ")
    second_username = input("Enter second username: ")

    if len(first_username) == 0 or len(second_username) == 0:
        print("All usernames must be filled")
        return ask_usernames()

    return [first_username, second_username]


if __name__ == '__main__':
    usernames = ask_usernames()
    print("Getting followers can take some time.")
    common_followers = get_users_common_followers(usernames)
    print("The list of common followers displaying below: ")
    print(common_followers)
