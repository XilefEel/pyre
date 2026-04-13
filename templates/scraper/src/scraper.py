import httpx
from bs4 import BeautifulSoup
from result import Err, Ok, Result

from models import ScrapedLink, ScrapedPage


def get_client() -> httpx.Client:
    return httpx.Client(timeout=10, verify=False)


def fetch_page(url: str) -> Result[ScrapedPage, str]:
    try:
        with get_client() as client:
            response = client.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.title.string if soup.title else "No title"
            body = soup.get_text(separator=" ", strip=True)

            return Ok(ScrapedPage(url=url, title=title, body=body))

    except httpx.HTTPError as e:
        return Err(f"HTTP error: {e}")

    except Exception as e:
        return Err(f"Unexpected error: {e}")


def fetch_links(url: str) -> Result[list[ScrapedLink], str]:
    try:
        with get_client() as client:
            response = client.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")
            links = [
                ScrapedLink(text=a.get_text(strip=True), href=a["href"])
                for a in soup.find_all("a", href=True)
            ]

            return Ok(links)

    except httpx.HTTPError as e:
        return Err(f"HTTP error: {e}")

    except Exception as e:
        return Err(f"Unexpected error: {e}")
