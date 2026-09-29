import re
from collections import Counter


def normalize_text(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("text должен быть строкой")
    return text.strip()


def analyze_text(text: str) -> dict:
    text = normalize_text(text)

    if not text:
        raise ValueError("text не должен быть пустым")

    words = re.findall(r"[A-Za-zА-Яа-яЁё0-9]+", text.lower())
    counter = Counter(words)

    return {
        "characters": len(text),
        "words": len(words),
        "unique_words": len(counter),
        "top_words": counter.most_common(5),
    }
