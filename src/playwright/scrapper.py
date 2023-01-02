import re
from playwright.sync_api import Page, expect
from bs4 import BeautifulSoup

def test_home(page: Page):
    page.goto("https://youtube.com")

    expect(page).to_have_title(re.compile("YouTube"))

    filename = "youtube.txt"

    html = page.content()

    soup = BeautifulSoup(html, "lxml")

    # get all contents
    soup2 = soup.find("ytd-rich-grid-renderer", {"class": "style-scope ytd-two-column-browse-results-renderer"})
    # parse the contents
    contents = BeautifulSoup(str(soup2), "lxml")

    # get all videos
    videos = contents.find_all("ytd-rich-item-renderer", {"class": "style-scope ytd-rich-grid-row"})
    
    # videos = BeautifulSoup(str(soup3), "lxml")
    for video in videos:
        # get video title
        link = video.find("a", {"id": "video-title-link"})
        title = link.get("title")
        channel = video.find("a", {"class": "yt-simple-endpoint style-scope yt-formatted-string"})
        meta = video.find_all("span", {"class": "inline-metadata-item style-scope ytd-video-meta-block"})

        with open(filename, "a") as f:
            f.write(f"제목: {title}\n")
            f.write(f"Link: https://youtube.com{link['href']}\n")
            f.write(f"채널 Name: {channel.text}\n")
            f.write(f"채널 Link: https://youtube.com{channel['href']}\n")
            for m in meta:
                f.write(f"{m.text}\n")
            # f.write(f"조회수: {meta}\n")
            # f.write(views + "\n")
            # f.write(time + "\n")
            # f.write(f"Duration: {duration.text}\n")
