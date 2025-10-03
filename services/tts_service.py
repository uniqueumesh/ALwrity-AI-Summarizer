from __future__ import annotations

import os
from typing import Optional


def text_to_speech(text: str) -> Optional[str]:
    """
    Use browser's built-in Web Speech API for text-to-speech.
    Returns the text to be spoken by the browser's TTS engine.
    """
    if not text or not text.strip():
        raise ValueError("Text cannot be empty for TTS conversion.")
    
    # Return the text for browser-based TTS
    return text.strip()


def get_available_voices() -> list[str]:
    """
    Get list of available voices for browser TTS.
    """
    return [
        "Default",     # Browser default voice
        "Female",      # Female voice
        "Male",        # Male voice
        "Child",       # Child voice
        "Senior"       # Senior voice
    ]
