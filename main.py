import re
from collections import Counter

HYPE_WORDS = [
    "OMG", "NO WAY", "BRO", "INSANE",
    "WHAT", "CRAZY", "WTF", "🔥", "LOL"
]

def detect_hype(messages):
    score = 0

    for message in messages:
        text = message.upper()

        for word in HYPE_WORDS:
            if word in text:
                score += 1

    return score

def find_viral_moments(chat_data, threshold=10):
    moments = []

    for timestamp, messages in chat_data.items():
        score = detect_hype(messages)

        if score >= threshold:
            moments.append({
                "timestamp": timestamp,
                "hype_score": score
            })

    return moments

if __name__ == "__main__":
    print("VICE CITY VIRAL CLIPPER")
    print("Hype detector ready!")
