from __future__ import annotations

import re
from typing import Tuple


WORD_RE = re.compile(r"\b\w+\b", re.UNICODE)


def count_words(text: str) -> int:
    if not text:
        return 0
    return len(WORD_RE.findall(text))


def clamp_to_word_limit(text: str, limit: int = 1000) -> str:
    if not text:
        return ""
    words = WORD_RE.findall(text)
    if len(words) <= limit:
        return text
    clamped = words[:limit]
    # Reconstruct with single spaces to avoid breaking words; preserves basic content
    return " ".join(clamped)


def can_submit(text: str, tone_choice: str, custom_tone: str) -> Tuple[bool, str]:
    # Returns (disabled, reason)
    if not text or not text.strip():
        return True, "Please add some text (≤ 1000 words)."
    if count_words(text) > 1000:
        return True, "Your input exceeds 1000 words. Please shorten it."
    if tone_choice == "Custom" and not (custom_tone and custom_tone.strip()):
        return True, "Custom tone can't be empty."
    return False, ""


