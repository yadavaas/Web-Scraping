import scrapy
from ..items import LearningItem
from scrapy.http import FormRequest

class Spider_quotes(scrapy.Spider):
    name = 'login'
    start_urls = ['https://quotes.toscrape.com/login']
    page_number = 2

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token' : token,
            'username' : 'dfdsaggds',
            'password' : 'fsfsdf'
        }, callback = self.start_scraping)

    def start_scraping(self, response):
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

        next_page = 'https://quotes.toscrape.com/page/'+str(Spider_quotes.page_number)+'/'

        if Spider_quotes.page_number<11:
            Spider_quotes.page_number += 1
            yield response.follow(next_page, callback=self.start_scraping)