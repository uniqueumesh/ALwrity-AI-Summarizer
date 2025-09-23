import streamlit as st
from ui.layout import render_layout


def main() -> None:
    st.set_page_config(page_title="ALwrity-AI-Summarizer", page_icon="📝", layout="centered")
    render_layout()


if __name__ == "__main__":
    main()


