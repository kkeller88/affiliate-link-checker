import os
from pathlib import Path
import requests

from scrapy.spiders import SitemapSpider
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Rule
from scrapy.http import Request, Response
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor

SOCIAL_DOMAINS = [
    'pinterest.com',
    'twitter.com',
    'instagram.com'
    ]
DOMAIN = os.environ['AFFILIATE_DOMAIN']

def getResponseCode(url):
    return 'Not implmented'

class SitemapScraper(SitemapSpider):
    name = 'sitemap-scraper'
    sitemap_urls = [os.path.join(
        'https://',
        DOMAIN,
        'sitemap.xml'
        )]

    def parse(self, response):
        extractor = LxmlLinkExtractor(
            deny_domains=[DOMAIN] + SOCIAL_DOMAINS
            )
        links = extractor.extract_links(response)
        for link in links:
            yield {
                'link': link.url,
                'page': response.url,
                'anchor_text': link.text,
                'response_code': getResponseCode(link.url)
                }

def crawl_pages(output_path):
    c = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0',
        'FEED_FORMAT': 'json',     # csv, json, xml
        'FEED_URI': output_path, #
    })
    c.crawl(SitemapScraper)
    c.start()

def build_temp_file_path(file):
    parent_dir = Path(__file__).parents[2]
    dir = os.path.join(parent_dir, 'data', 'tmp')
    file_path = os.path.join(dir, file)
    return file_path

output_path = build_temp_file_path('test.json')
crawl_pages(output_path)
