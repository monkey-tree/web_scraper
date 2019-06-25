import sys
import re
import chardet
import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError

def download(url, user_agent = 'wswp', num_retries = 2, charset = 'utf-8'):
    print("Downloading: {}".format(url))
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        print("Download starts.")
        resp = urllib.request.urlopen(request)
        print("Downloads completes.")
        cs = resp.headers.get_content_charset()
        print("Charset gotten.")
        html_raw = resp.read()
        print("html read is done.")
        if not cs:
            print("Charset detection start.")
            csdet = chardet.detect(html_raw)
            print("Charset detection completes.")
            cs = csdet['encoding']
            print("Charset: {}".format(cs))

        html = html_raw.decode(cs)
        resp.close

    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error: {}'.format(e.reason))
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code <600:
                return download(url, num_retries - 1)
    return html


def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url)
    # extract the sitemap links
    print("Sitemap links extraction starts.")
    links = re.findall ('<loc>(.*?)</loc>', sitemap)
    print("Sitemap links extraction ends.")
    for link in links:
        html = download(link)
        # scrape html here



def main():
    url = 'http://example.webscraping.com/sitemap.xml'
    # html = download(url)
    # print("Page download as: \n {}".format(html))
    crawl_sitemap(url)
    sys.exit(0)

if '__main__' == __name__:
    main()
