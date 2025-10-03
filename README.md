# ALwrity-AI-Summarizer
An ultra-fast, accurate AI summarization tool that turns long articles, PDFs, web pages, and documents into clear, actionable summaries. Designed for creators, marketers, students, and busy professionals who need the gist without the grind.
## ALwrity-AI-Summarizer

Ultra-fast, accurate AI summarization that turns long text into clear, actionable summaries. Built for creators, marketers, students, and busy professionals who need the gist without the grind.

This is a Streamlit app that uses the Gemini 2.5 Flash model for AI processing. The API key is configured server-side, so users just need to paste their text and get instant summaries.

### Key Features
- **Plain text input** up to 1000 words (with live counter)
- **Result format**: Paragraph or Bullet points
- **Tone**: Formal, Friendly, Casual, Professional, Diplomatic, Confident, or Custom
- **Copy button** to copy your summary to the clipboard
- **No setup required**: Just paste and summarize

### Requirements
- Python 3.10+
- Gemini API key (configured as environment variable `GEMINI_API_KEY`)

### Quick Start
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Run the app:
```bash
streamlit run app.py
```
3. In your browser, paste your text (≤1000 words), choose format and tone, and click Summarize. Use the Copy button to copy the result.

### How It Works
- The app builds a clear, constrained prompt that matches your chosen format and tone, then calls the Gemini 2.5 Flash model.
- Your text is processed by Gemini and is not stored locally by this app.

### Configuration (Required for Deployment)
- **Gemini API Key**: Set the environment variable `GEMINI_API_KEY` with your Gemini API key.
  - Example (PowerShell):
  ```bash
  $env:GEMINI_API_KEY = "your-gemini-api-key-here"
  streamlit run app.py
  ```
- **Model Selection**: Set `ALWRITY_GEMINI_MODEL` to use a different Gemini model (default is `gemini-2.5-flash`).

### Usage Tips
- Keep inputs focused. Short, relevant text produces the best summaries.
- For bullet points, aim for clear, discrete ideas.
- Custom tone accepts short descriptors (e.g., "persuasive", "academic", "playful").

### Troubleshooting
- "Please add some text (≤ 1000 words)": Paste text; keep it within the limit.
- "Your input exceeds 1000 words": The app enforces the limit; shorten your input.
- "Gemini API key not configured": Set the `GEMINI_API_KEY` environment variable with your Gemini API key.
- Copy button does nothing: Your browser may block clipboard access. Click on the page once and try again; the app includes a fallback that simulates copying.

### Privacy & Security
- The app does not store your input text locally. Content is sent securely to Google's Gemini API for processing.

### Project Structure (Overview)
```
app.py                     # Streamlit entry point
ui/layout.py               # UI layout and interactions
core/validation.py         # Input word count and submission gating
core/prompt.py             # Prompt builder (format & tone aware)
services/gemini_client.py  # Gemini API client (server-side key)
requirements.txt           # Python dependencies
```

### License
See `LICENSE` for details.
