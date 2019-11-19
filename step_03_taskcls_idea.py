import aiohttp
from lxml import etree
from io import StringIO

from celeryapp import celeryapp


class BaseCrawler:
    def __init__(self):
        # TODO: высосать из пальца состояние
        # Ибо найдутся те, кто скажет "зачем класс?"
        # и формально будет прав
        pass

    async def build_kwargs(self):
        return dict(
            method=self.method,
            url=self.url,
        )

    async def get_etree_data(self):
        kwargs = await self.build_kwargs()
        async with aiohttp.ClientSession() as client:
            async with client.request(**kwargs) as raw_response:
                response_text = await raw_response.text()

        parser = etree.HTMLParser()
        return etree.parse(StringIO(response_text), parser)

    async def execute(self):
        etree = await self.get_etree_data()
        return etree.xpath(self.xpath)

    @classmethod
    async def task(cls):
        self = cls()
        result = await self.execute()
        print(result)


@celeryapp.taskcls(name='opennet_news')
class OpennetNews(BaseCrawler):
    method = 'GET'
    url = 'https://www.opennet.ru/opennews/'
    xpath = r"//a[@class='title2']/text()"


@celeryapp.taskcls(name='habr_posts')
class HabrPosts(BaseCrawler):
    method = 'GET'
    url = 'https://habr.com/ru/top/'
    xpath = r"//h2[@class='post__title']/a/text()"
