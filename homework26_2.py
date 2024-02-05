import aiohttp
import asyncio
import json

async def fetch_comments(subreddit):
    url = f"https://api.pushshift.io/reddit/comment/search/?subreddit={subreddit}"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            try:
                data = await response.json()
                return data.get('data', [])
            except json.JSONDecodeError:
                print("Error decoding JSON response.")
                return []

async def main():
    subreddit = "your_subreddit_here"
    comments = await fetch_comments(subreddit)

    if not comments:
        print(f"No comments retrieved for subreddit '{subreddit}'.")
        return

    sorted_comments = sorted(comments, key=lambda x: x.get('created_utc', 0))

    with open('reddit_comments.json', 'w') as file:
        json.dump(sorted_comments, file, indent=2)

if __name__ == "__main__":
    asyncio.run(main())
