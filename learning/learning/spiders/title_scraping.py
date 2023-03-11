import scrapy

class Spider_quotes(scrapy.Spider):
    name = 'title_scrap'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response, **kwargs):
        title = response.css('title::text').extract()
        yield {'titletext' : title}