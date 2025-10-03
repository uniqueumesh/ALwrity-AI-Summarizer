# ALwrity-AI-Summarizer
An ultra-fast, accurate AI summarization tool that turns long articles, PDFs, web pages, and documents into clear, actionable summaries. Designed for creators, marketers, students, and busy professionals who need the gist without the grind.
## ALwrity-AI-Summarizer

Ultra-fast, accurate AI summarization that turns long text into clear, actionable summaries. Built for creators, marketers, students, and busy professionals who need the gist without the grind.

This is a Streamlit app that connects to the ALwrity backend API for AI processing. No API keys or configuration needed - just paste your text and get instant summaries.

### Key Features
- **Plain text input** up to 1000 words (with live counter)
- **Result format**: Paragraph or Bullet points
- **Tone**: Formal, Friendly, Casual, Professional, Diplomatic, Confident, or Custom
- **Copy button** to copy your summary to the clipboard
- **No setup required**: Just paste and summarize

### Requirements
- Python 3.10+
- Internet connection for backend API access

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
- The app builds a clear, constrained prompt that matches your chosen format and tone, then sends it to the ALwrity backend API for processing.
- Your text is sent securely to the backend API and is not stored locally by this app.

### Configuration (Optional)
- Backend API URL: set the environment variable `ALWRITY_BACKEND_URL` to use a different backend endpoint (default is `https://api.alwrity.com/summarize`).
  - Example (PowerShell):
  ```bash
  $env:ALWRITY_BACKEND_URL = "https://your-backend.com/summarize"
  streamlit run app.py
  ```

### Usage Tips
- Keep inputs focused. Short, relevant text produces the best summaries.
- For bullet points, aim for clear, discrete ideas.
- Custom tone accepts short descriptors (e.g., "persuasive", "academic", "playful").

### Troubleshooting
- "Please add some text (≤ 1000 words)": Paste text; keep it within the limit.
- "Your input exceeds 1000 words": The app enforces the limit; shorten your input.
- Backend API error: Check your internet connection and try again.
- Copy button does nothing: Your browser may block clipboard access. Click on the page once and try again; the app includes a fallback that simulates copying.

### Privacy & Security
- The app does not store your input text locally. Content is sent securely to the ALwrity backend API for processing.

### Project Structure (Overview)
```
app.py                     # Streamlit entry point
ui/layout.py               # UI layout and interactions
core/validation.py         # Input word count and submission gating
core/prompt.py             # Prompt builder (format & tone aware)
services/gemini_client.py  # Backend API client
requirements.txt           # Python dependencies
```

### License
See `LICENSE` for details.
