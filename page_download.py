import sys
import re
import time
import chardet
import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError

def download(url, user_agent = 'wswp', num_retries = 2, charset = 'utf-8'):
    request.add_header('User-agent', user_agent)
    try:
        print("Download starts.")
        time_start = time.time()
        resp = urllib.request.urlopen(request)
        print("Downloads completes.")
        print("Downloads completes and eclips {}s.".format(time.time() - time_start))
        time_start = time.time()
        cs = resp.headers.get_content_charset()
        print("Charset gotten.")
        print("Charset gotten and eclips {}s".format(time.time() - time_start))
        html_raw = resp.read()
        print("html read is done.")
        if not cs:
            print("Charset detection start.")
            time_start = time.time()
            csdet = chardet.detect(html_raw)
            print("Charset detection completes.")
            cs = csdet['encoding']
            print("Charset: {}".format(cs))
            print("Charset: {} and eclips {}s.".format(cs, time.time() - time_start))

        html = html_raw.decode(cs)
        resp.close

def crawl_sitemap(url):
    # extract the sitemap links
    print("Sitemap links extraction starts.")
    links = re.findall ('<loc>(.*?)</loc>', sitemap)
    print("links extracted: \n {}".format(links))
    print("Sitemap links extraction ends.")
    for link in links:
        html = download(link)