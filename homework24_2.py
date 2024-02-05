import requests
import concurrent.futures

def download_comments(subreddit):
    url = f"https://api.pushshift.io/reddit/comment/search/?subreddit={subreddit}"
    response = requests.get(url)
    return response.json()

def download_comments_concurrent(subreddit, executor):
    with executor() as pool:
        result = pool.submit(download_comments, subreddit)
        return result.result()

if __name__ == "__main__":
    subreddit_name = "python"
    
    with concurrent.futures.ThreadPoolExecutor() as thread_pool:
        thread_result = download_comments_concurrent(subreddit_name, concurrent.futures.ThreadPoolExecutor)

    with concurrent.futures.ProcessPoolExecutor() as process_pool:
        process_result = download_comments_concurrent(subreddit_name, concurrent.futures.ProcessPoolExecutor)

    with open("comments.json", "w") as file:
        file.write(str(thread_result))
