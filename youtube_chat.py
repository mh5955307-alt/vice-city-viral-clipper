import requests
from config import YOUTUBE_API_KEY

def get_live_chat_messages(live_chat_id, page_token=None):
    url = "https://www.googleapis.com/youtube/v3/liveChat/messages"

    params = {
        "liveChatId": live_chat_id,
        "part": "snippet,authorDetails",
        "key": YOUTUBE_API_KEY
    }

    if page_token:
        params["pageToken"] = page_token

    response = requests.get(url, params=params, timeout=20)
    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    print("YouTube Chat Reader Ready")
