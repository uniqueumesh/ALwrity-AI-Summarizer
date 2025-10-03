from __future__ import annotations

import os
from typing import Dict, Any
import requests


BACKEND_API_URL = os.environ.get("ALWRITY_BACKEND_URL", "https://api.alwrity.com/summarize")


def summarize_with_gemini(prompt: str) -> str:
    """
    Send summarization request to backend API instead of direct Gemini API.
    """
    try:
        response = requests.post(
            BACKEND_API_URL,
            json={"prompt": prompt},
            timeout=30,
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        
        data: Dict[str, Any] = response.json()
        
        if "summary" not in data:
            raise RuntimeError("Invalid response format from backend API.")
            
        summary = data["summary"]
        if not summary or not summary.strip():
            raise RuntimeError("Empty summary returned from backend API.")
            
        return summary.strip()
        
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Backend API error: {str(e)}")
    except KeyError as e:
        raise RuntimeError(f"Invalid response format: missing {e}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error: {str(e)}")


