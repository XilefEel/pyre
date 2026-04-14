from result import Err, Ok
from scraper import fetch_links, fetch_page


def main() -> None:
    url = "https://example.com"

    print(f"Scraping {url}...\n")

    match fetch_page(url):
        case Ok(page):
            print(f"Title: {page.title}")
            print(f"Body preview: {page.body[:200]}")
        case Err(e):
            print(f"Failed to fetch page: {e}")

    print("\nLinks found:")
    match fetch_links(url):
        case Ok(links):
            for link in links:
                print(f"{link.text} -> {link.href}")
        case Err(e):
            print(f"Failed to fetch links: {e}")


if __name__ == "__main__":
    main()
