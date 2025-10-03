from __future__ import annotations

import os
from typing import Optional

import google.generativeai as genai


GEMINI_MODEL = os.environ.get("ALWRITY_GEMINI_MODEL", "gemini-2.5-flash")


def summarize_with_gemini(prompt: str) -> str:
    """
    Use Gemini API with server-side API key from environment variable.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Gemini API key not configured. Please set GEMINI_API_KEY environment variable.")

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(GEMINI_MODEL)
        response = model.generate_content(prompt)

        # The SDK can return candidates; prefer text
        text: Optional[str] = None
        if hasattr(response, "text") and response.text:
            text = response.text
        elif hasattr(response, "candidates") and response.candidates:
            for c in response.candidates:
                try:
                    text = c.content.parts[0].text  # type: ignore[attr-defined]
                    if text:
                        break
                except Exception:
                    continue

        if not text:
            raise RuntimeError("No summary returned from the model.")

        return text.strip()
        
    except Exception as e:
        raise RuntimeError(f"Gemini API error: {str(e)}")


