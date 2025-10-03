import streamlit as st
from streamlit.components.v1 import html as _html
from core.validation import clamp_to_word_limit, count_words, can_submit
from core.prompt import build_prompt
from services.gemini_client import summarize_with_gemini


TONE_OPTIONS = [
    "Formal",
    "Friendly",
    "Casual",
    "Professional",
    "Diplomatic",
    "Confident",
    "Custom",
]

LANGUAGE_OPTIONS = [
    "English",
    "Spanish",
    "French",
    "German",
    "Italian",
    "Portuguese",
    "Russian",
    "Chinese (Simplified)",
    "Chinese (Traditional)",
    "Japanese",
    "Korean",
    "Arabic",
    "Hindi",
    "Dutch",
    "Swedish",
    "Norwegian",
    "Danish",
    "Finnish",
    "Polish",
    "Czech",
    "Hungarian",
    "Romanian",
    "Bulgarian",
    "Croatian",
    "Slovak",
    "Slovenian",
    "Greek",
    "Turkish",
    "Hebrew",
    "Thai",
    "Vietnamese",
    "Indonesian",
    "Malay",
    "Filipino",
    "Ukrainian",
    "Belarusian",
    "Lithuanian",
    "Latvian",
    "Estonian",
    "Custom",
]


def render_layout() -> None:
    if "summary" not in st.session_state:
        st.session_state.summary = ""

    st.title("ALwrity-AI-Content-Summarizer")
    st.caption("Turn long text into clear, actionable summaries in seconds.")

    input_text = st.text_area(
        "Input Text (max 1000 words)",
        placeholder="Paste up to 1000 words of text to summarize...",
        height=240,
        key="input_text",
    )
    trimmed_text = clamp_to_word_limit(input_text, limit=1000)
    if trimmed_text != input_text:
        st.warning("Input truncated to 1000 words.")
    word_count = count_words(trimmed_text)
    counter_color = "red" if word_count > 1000 else "gray"
    st.markdown(f"<span style='color:{counter_color}'>Words: {word_count}/1000</span>", unsafe_allow_html=True)

    st.subheader("Options")
    col1, col2, col3 = st.columns(3)
    with col1:
        format_choice = st.radio(
            "Result format",
            options=["Paragraph", "Bullet points"],
            index=0,
            horizontal=False,
            key="format_choice",
            help="Choose how the summary should look.",
        )
    with col2:
        tone_choice = st.selectbox(
            "Tone",
            options=TONE_OPTIONS,
            index=0,
            help="Select a tone for the summary.",
            key="tone_choice",
        )
        custom_tone = ""
        if tone_choice == "Custom":
            custom_tone = st.text_input(
                "Custom tone",
                placeholder="e.g., persuasive, academic, playful…",
                key="custom_tone",
            )
    with col3:
        language_choice = st.selectbox(
            "Language",
            options=LANGUAGE_OPTIONS,
            index=0,
            help="Select the language for the summary.",
            key="language_choice",
        )
        custom_language = ""
        if language_choice == "Custom":
            custom_language = st.text_input(
                "Custom language",
                placeholder="e.g., Swahili, Bengali, Tamil…",
                key="custom_language",
            )

    st.markdown("---")
    submit_disabled, submit_reason = can_submit(
        text=trimmed_text,
        tone_choice=tone_choice,
        custom_tone=custom_tone,
        language_choice=language_choice,
        custom_language=custom_language,
    )

    if submit_disabled and submit_reason:
        st.info(submit_reason)

    summarize = st.button("Summarize", type="primary", disabled=submit_disabled)

    if summarize:
        with st.spinner("Summarizing…"):
            try:
                prompt = build_prompt(
                    text=trimmed_text,
                    format_choice=format_choice,
                    tone_choice=tone_choice,
                    custom_tone=custom_tone,
                    language_choice=language_choice,
                    custom_language=custom_language,
                )
                result = summarize_with_gemini(prompt=prompt)
                st.session_state.summary = result.strip()
            except Exception as exc:  # noqa: BLE001
                st.session_state.summary = ""
                st.error(str(exc))

    st.subheader("Summary")
    if st.session_state.summary:
        st.text_area(
            "Summary",
            value=st.session_state.summary,
            height=220,
            label_visibility="collapsed",
            key="summary_output",
        )
        _render_copy_button(st.session_state.summary)
    else:
        st.caption("Your summary will appear here after processing.")


def _render_copy_button(text: str) -> None:
    import json
    import uuid

    safe_text_js = json.dumps(text)
    btn_id = f"copy_btn_{uuid.uuid4().hex}"
    _html(
        f"""
        <button id="{btn_id}" style="margin-top:8px;">Copy</button>
        <script>
        (function() {{
          const btn = document.getElementById('{btn_id}');
          const text = {safe_text_js};
          if (!btn) return;
          btn.addEventListener('click', async () => {{
            try {{
              await navigator.clipboard.writeText(text);
            }} catch (e) {{
              const ta = document.createElement('textarea');
              ta.value = text;
              ta.style.position = 'fixed';
              ta.style.left = '-9999px';
              document.body.appendChild(ta);
              ta.focus();
              ta.select();
              try {{ document.execCommand('copy'); }} catch (e2) {{ /* ignore */ }}
              document.body.removeChild(ta);
            }}
            const original = btn.innerText;
            btn.innerText = 'Copied!';
            setTimeout(() => btn.innerText = original, 1200);
          }});
        }})();
        </script>
        """,
        height=46,
    )


