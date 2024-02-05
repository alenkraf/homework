import requests
import threading

def download_comments(subreddit):
    url = f"https://api.pushshift.io/reddit/comment/search/?subreddit={subreddit}"
    response = requests.get(url)
    return response.json()

def download_comments_threaded(subreddit):
    result = None
    lock = threading.Lock()

    def download_and_store():
        nonlocal result
        data = download_comments(subreddit)
        with lock:
            result = data

    thread = threading.Thread(target=download_and_store)
    thread.start()
    thread.join()

    return result

# Example usage:
if __name__ == "__main__":
    subreddit_name = "python"
    comments_data = download_comments_threaded(subreddit_name)

    with open("comments.json", "w") as file:
        file.write(str(comments_data))
