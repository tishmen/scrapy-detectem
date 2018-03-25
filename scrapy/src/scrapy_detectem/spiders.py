import json

from datetime import datetime

from scrapy import Spider
from scrapy.exceptions import NotConfigured
from scrapy.http import FormRequest

from scrapy_detectem.items import DetectemLoader


class DetectemSpider(Spider):

    name = 'detectem'

    def __init__(self, crawler, start_urls, detectem_url, *args, **kwargs):
        self.crawler = crawler
        self.start_urls = start_urls
        self.detectem_url = detectem_url

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        start_urls = kwargs.pop('start_urls', None)
        if not start_urls:
            raise NotConfigured('start_urls not found.')
        try:
            start_urls = json.loads(start_urls)
        except ValueError:
            raise NotConfigured('start_urls not valid.')
        detectem_url = crawler.settings.get('DETECTEM_URL')
        if not detectem_url:
            raise NotConfigured('DETECTEM_URL not found.')
        return cls(crawler, start_urls, detectem_url, *args, **kwargs)

    def _load_item(self, response):
        loader = DetectemLoader()
        loader.add_value('url', response.url)
        loader.add_value('data', json.loads(response.body_as_unicode()))
        loader.add_value('timestamp', datetime.utcnow().isoformat())
        return loader.load_item()

    def start_requests(self):
        for url in self.start_urls:
            yield FormRequest(
                self.detectem_url, method='POST', formdata={'url': url}
            )

    def parse(self, response):
        yield self._load_item(response)
