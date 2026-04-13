from dataclasses import dataclass


@dataclass(frozen=True)
class ScrapedPage:
    url: str
    title: str
    body: str


@dataclass(frozen=True)
class ScrapedLink:
    text: str
    href: str
