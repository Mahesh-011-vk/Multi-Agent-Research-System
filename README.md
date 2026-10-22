# Multi-Agent Research System

A research assistant that searches the web, reads selected source pages, writes an evidence-led report, and asks a critic to review it. Use the Streamlit interface or run the research pipeline from the command line.

## Features

- **Web research agent** finds recent sources with Tavily.
- **Webpage reader agent** extracts text from up to three relevant pages.
- **Report writer** creates a structured report with findings, limitations, a conclusion, and source URLs.
- **Critic pipeline** reviews the report for accuracy, evidence, completeness, and clarity.
- **Streamlit interface** displays reports, evidence, and critic feedback, with Markdown and JSON downloads.

The agents and writer use Google's `gemini-2.5-flash` model through LangChain.

## Requirements

- Python 3.10 or newer
- A [Google AI API key](https://aistudio.google.com/app/apikey)
- A [Tavily API key](https://tavily.com/)

## Setup

Clone the repository and enter its directory:

```bash
git clone https://github.com/Mahesh-011-vk/Multi-Agent-Research-System.git
cd Multi-Agent-Research-System
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Create a `.env` file in the project root. Set your Google key as either `GOOGLE_API_KEY` or `GEMINI_API_KEY`, and set your Tavily key as `TAVILY_API_KEY`:

```dotenv
GOOGLE_API_KEY=your_google_ai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Keep `.env` private; do not commit API keys.

## Run the app

Start the Streamlit web interface:

```bash
streamlit run app.py
```

Open the local URL printed in the terminal, enter a focused research question, and select **Run research**. Completed reports can be downloaded from the interface. The latest results are also saved to `research_report.json` in the working directory.

## Run from the command line

Run the pipeline directly:

```bash
python pipeline.py
```

Enter a topic when prompted. The pipeline prints the search results, extracted webpage content, report, and critic feedback, then writes the full results to `research_report.json`.

## Project structure

| File | Purpose |
| --- | --- |
| `app.py` | Streamlit research interface |
| `pipeline.py` | Coordinates the search, reading, writing, and critic stages |
| `agent.py` | Configures the Gemini-backed agents and report/critic chains |
| `tools.py` | Tavily web search and webpage extraction tools |
| `requirements.txt` | Python dependencies |

## Notes

- Research requires network access and valid Google AI and Tavily API keys. Provider quotas and usage limits may apply.
- Search results and extracted page content depend on source availability and may be incomplete. Verify important claims against the linked sources.
- The webpage reader retrieves publicly accessible HTTP/HTTPS pages; some sites may block automated requests.
