import requests
from bs4 import BeautifulSoup

ptt_url = "https://www.ptt.cc/bbs/"
board = "Stock"


def get_paragraph_title_href(url):

    title_list = []
    for title in get_soup(url).find_all("div", {"class": "title"}):
        if title.a is None:
            continue
        p_d = dict()
        p_d["title"] = title.a.text
        p_d["href"] = title.a["href"]
        title_list.append(p_d)
    return title_list


def get_soup(url):
    if url.startswith("/bbs/"):
        request_url = ptt_url + url.lstrip("/bbs/")
    else:
        request_url = ptt_url + url
    response = requests.get(request_url, cookies={"over18": "1"})
    # print(r.status_code)
    # print(response.text)
    return BeautifulSoup(response.text, "html.parser")


def get_upper_page(url):
    soup = get_soup(url)
    return soup.find_all("a", {"class": "btn wide"})[1]["href"]


if __name__ == "__main__":
    print(get_paragraph_title_href(get_upper_page("Stock")))
