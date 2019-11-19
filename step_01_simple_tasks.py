import aiohttp
from lxml import etree
from io import StringIO

from celeryapp import celeryapp


@celeryapp.task(name='opennet_news')
async def opennet_news():
    url = 'https://www.opennet.ru/opennews/'
    async with aiohttp.ClientSession() as client:
        async with client.get(url=url) as raw_response:
            response_text = await raw_response.text()

    parser = etree.HTMLParser()
    response = etree.parse(StringIO(response_text), parser)
    print(response.xpath(r"//a[@class='title2']/text()"))


@celeryapp.task(name='habr_posts')
async def habr_posts():
    url = 'https://habr.com/ru/top/'
    async with aiohttp.ClientSession() as client:
        async with client.get(url=url) as raw_response:
            response_text = await raw_response.text()

    parser = etree.HTMLParser()
    response = etree.parse(StringIO(response_text), parser)
    print(response.xpath(r"//h2[@class='post__title']/a/text()"))
