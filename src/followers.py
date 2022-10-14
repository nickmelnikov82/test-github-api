import json
import requests

from src.list_helpers import intersection

PER_PAGE = 100


def get_users_common_followers(usernames):
    users_followers = []
    for username in usernames:
        user_followers = get_user_followers_usernames(username)
        users_followers.append(user_followers)

    return intersection(users_followers)


def get_user_followers_usernames(username):
    return get_followers_usernames(get_user_followers(username))


def get_followers_usernames(followers):
    return [follower.get("login") for follower in followers]


def get_user_followers(username):
    page = 1
    is_next_page_available = True
    followers = []

    while is_next_page_available:
        result = get_user_followers_on_page(username, page, PER_PAGE)
        followers.extend(result.get("followers"))
        page += 1
        is_next_page_available = result.get("is_next_page_available")

    return followers


def get_user_followers_on_page(username, page, per_page):
    response = requests.get(f"https://api.github.com/users/{username}/followers?page={page}&per_page={per_page}")
    followers = json.loads(response.text)
    is_next_page_available = len(followers) == per_page
    return {"followers": followers, "is_next_page_available": is_next_page_available}

