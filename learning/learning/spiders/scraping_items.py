import scrapy
from ..items import LearningItem

class Spider_quotes(scrapy.Spider):
    name = 'items_scrap'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        items = LearningItem()
        div_quote = response.css('div.quote')

        for quote in div_quote:
            title = quote.css('span.text::text').extract()
            author = quote.css('small.author::text').extract()
            tags = quote.css('a.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tags'] = tags

            yield items

        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)