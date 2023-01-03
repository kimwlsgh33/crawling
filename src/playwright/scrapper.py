import re
from playwright.sync_api import Page, expect
from bs4 import BeautifulSoup
# my modules
from date_fs import get_file_path
from pyutil import get_view_count, get_upload_date

def test_home(page: Page):
    page.goto("https://youtube.com")

    expect(page).to_have_title(re.compile("YouTube"))

    html = page.content()

    soup = BeautifulSoup(html, "lxml")

    # get all contents
    soup2 = soup.find("ytd-rich-grid-renderer", {"class": "style-scope ytd-two-column-browse-results-renderer"})
    # parse the contents
    contents = BeautifulSoup(str(soup2), "lxml")

    # get all videos
    videos = contents.find_all("ytd-rich-item-renderer", {"class": "style-scope ytd-rich-grid-row"})

    filename = "youtube"

    file_path = get_file_path(filename)
    with open(file_path, "w") as f:
        # videos = BeautifulSoup(str(soup3), "lxml")
        for video in videos:
            # get video title
            link = video.find("a", {"id": "video-title-link"})
            res_title = link.get("title")
            channel = video.find("a", {"class": "yt-simple-endpoint style-scope yt-formatted-string"})
            meta = video.find_all("span", {"class": "inline-metadata-item style-scope ytd-video-meta-block"})

            view_count = get_view_count(meta[0].text)
            upload_date = get_upload_date(meta[1].text)

            ###############################
            ### save the data to a file ###
            ###############################
            f.write("#" * 50)
            f.write("\n")
            f.write(f"제목: {res_title}\n")
            f.write(f"Link: {link.get('href')}\n")
            f.write(f"채널 Name: {channel.get_text()}\n")
            f.write(f"채널 Link: {channel.get('href')}\n")
            # f.write(f"조회수: {meta[0].text}\n")
            # f.write(f"게시일: {meta[-1].text}\n")
            f.write(f"조회수: {view_count}\n")
            f.write(f"게시일: {upload_date}\n")
        f.close()






