
import os
import json
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")
if not api_key:
    raise ValueError(
        "TAVILY_API_KEY is missing. Check your project-root .env file."
    )

tavily = TavilyClient(api_key=api_key)


@tool
def web_search(query: str) -> str:
    """Search the web and return relevant titles, URLs, and snippets."""
    results = tavily.search(query=query, max_results=5)
    return json.dumps(results, ensure_ascii=False)


@tool
def scrape_url(url: str) -> str:
    """Extract readable text from a publicly accessible webpage."""
    try:
        response = requests.get(
            url,
            timeout=20,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")

        for element in soup(
            ["script", "style", "nav", "footer", "header", "noscript"]
        ):
            element.decompose()

        title = soup.title.get_text(strip=True) if soup.title else "Untitled"
        content = soup.get_text(separator=" ", strip=True)

        return f"Title: {title}\nURL: {url}\n\nContent:\n{content[:12000]}"

    except requests.RequestException as exc:
        return f"Unable to scrape {url}: {exc}"
