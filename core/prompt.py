from __future__ import annotations


def build_prompt(text: str, format_choice: str, tone_choice: str, custom_tone: str) -> str:
    chosen_tone = custom_tone.strip() if tone_choice == "Custom" and custom_tone else tone_choice
    target_format_instruction = (
        "Write a single cohesive paragraph."
        if format_choice == "Paragraph"
        else "Write concise bullet points, one idea per line."
    )

    prompt = f"""
You are an expert editor and summarizer. Summarize the user's text faithfully.

Objectives:
- Capture key points and important details.
- Remove fluff and redundancy.
- Do not add facts not present in the source text.

Constraints:
- Tone: {chosen_tone}.
- Format: {format_choice}. {target_format_instruction}
- Keep it concise and readable on a mobile screen.

User's text:
"""
    prompt = prompt.strip() + "\n" + text.strip()
    return prompt


