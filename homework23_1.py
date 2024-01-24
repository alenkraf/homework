import requests

def get_robot(url: str):
    robot_content = requests.get(url + "robots.txt").text

    try:
        with open("my_robots.txt", "r", encoding="utf-8") as r_r:
            existing_content = r_r.read()
    except FileNotFoundError:
        existing_content = ""

    with open("my_robots.txt", "w", encoding="utf-8") as a_r:
        separator = "===================================================="
        a_r.write(separator + "\n")
        a_r.write(existing_content)
        a_r.write(robot_content)
        a_r.write(separator + "\n")

wiki_url = "https://uk.wikipedia.org/"
twitter_url = "https://twitter.com/"
youtube_url = "https://www.youtube.com/"

get_robot(wiki_url)
get_robot(twitter_url)
get_robot(youtube_url)
