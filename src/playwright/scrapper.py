import re
from playwright.sync_api import Page, expect
from bs4 import BeautifulSoup

def test_home(page: Page):
    page.goto("https://youtube.com")

    expect(page).to_have_title(re.compile("YouTube"))

    filename = "youtube.txt"

    html = page.content()

    soup = BeautifulSoup(html, "lxml")

    soup2 = soup.find("ytd-rich-grid-renderer", {"class": "style-scope ytd-two-column-browse-results-renderer"})

    contents = BeautifulSoup(str(soup2), "lxml")

    soup3 = contents.find_all("ytd-rich-item-renderer", {"class": "style-scope ytd-rich-grid-row"})
    
    videos = BeautifulSoup(str(soup3), "lxml")

    soup4 = videos.find_all("div", {"id": "meta"})

    meta = BeautifulSoup(str(soup4), "lxml")

    soup5 = meta.find_all("a", {"id": "video-title-link"})
    link = BeautifulSoup(str(soup5), "lxml")

    with open(filename, "w") as f:
        for i in link.find_all("a"):
            f.write(i.get("title"))
            f.write("\n")
        # f.write(str(title))
