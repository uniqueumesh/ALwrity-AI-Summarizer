# ALwrity-AI-Summarizer
An ultra-fast, accurate AI summarization tool that turns long articles, PDFs, web pages, and documents into clear, actionable summaries. Designed for creators, marketers, students, and busy professionals who need the gist without the grind.
## ALwrity-AI-Summarizer

Ultra-fast, accurate AI summarization that turns long text into clear, actionable summaries. Built for creators, marketers, students, and busy professionals who need the gist without the grind.

This is a Streamlit app using the Gemini 2.5 Flash model. It is BOYK (Bring Your Own Key): you enter your own Gemini API key in the app. No keys or inputs are stored.

### Key Features
- **Plain text input** up to 1000 words (with live counter)
- **Result format**: Paragraph or Bullet points
- **Tone**: Formal, Friendly, Casual, Professional, Diplomatic, Confident, or Custom
- **Copy button** to copy your summary to the clipboard
- **BOYK**: Your Gemini API key stays in your session only

### Requirements
- Python 3.10+
- A Gemini API key

### Get a Gemini API Key
1. Create or sign in to your Google account.
2. Visit the Gemini developer console (search for "Google Generative AI API key").
3. Create an API key and copy it. You will paste it into the app when prompted.

### Quick Start
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Run the app:
```bash
streamlit run app.py
```
3. In your browser, enter your Gemini API key in the app, paste your text (≤1000 words), choose format and tone, and click Summarize. Use the Copy button to copy the result.

### How It Works
- The app builds a clear, constrained prompt that matches your chosen format and tone, then calls the Gemini 2.5 Flash model and displays the result.
- Your API key and text are kept in the Streamlit session only and are not saved to disk by this app.

### Configuration (Optional)
- Model override: set the environment variable `ALWRITY_GEMINI_MODEL` to use a different model name (default is `gemini-2.5-flash`).
  - Example (PowerShell):
  ```bash
  $env:ALWRITY_GEMINI_MODEL = "gemini-2.5-flash"
  streamlit run app.py
  ```

### Usage Tips
- Keep inputs focused. Short, relevant text produces the best summaries.
- For bullet points, aim for clear, discrete ideas.
- Custom tone accepts short descriptors (e.g., "persuasive", "academic", "playful").

### Troubleshooting
- "Please enter your API key": Enter your Gemini API key in the API Key section.
- "Please add some text (≤ 1000 words)": Paste text; keep it within the limit.
- "Your input exceeds 1000 words": The app enforces the limit; shorten your input.
- Invalid key / API error: Double-check your key and connectivity; try again.
- Copy button does nothing: Your browser may block clipboard access. Click on the page once and try again; the app includes a fallback that simulates copying.

### Privacy & Security
- The app does not store or log your API key or input text beyond the active session. Content is sent to Google’s API for processing.

### Project Structure (Overview)
```
app.py                     # Streamlit entry point
ui/layout.py               # UI layout and interactions
core/validation.py         # Input word count and submission gating
core/prompt.py             # Prompt builder (format & tone aware)
services/gemini_client.py  # Gemini client (uses your API key)
requirements.txt           # Python dependencies
```

### License
See `LICENSE` for details.
