import scrapy
from ..items import FlipkartItem

class Spider_mobile(scrapy.Spider):
    name = 'mobile_scrap'
    start_urls = ['https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Realme&p%5B%5D=facets.brand%255B%255D%3DPOCO&page=1']
    page_number = 2

    def parse(self, response):
        items = FlipkartItem()
        section = response.css('._2kHMtA')

        for itr in section:
            name = itr.css('div._4rR01T::text').extract()
            actual_price = itr.css('._1_WHN1::text').extract()
            price_without_discount = itr.css('._27UcVY::text').extract()
            discount = itr.css('._3Ay6Sb span::text').extract()
            specification = itr.css('li.rgWa7D::text').extract()
            rating = itr.css('div._3LWZlK::text').extract()
            total_ratings = itr.css('._2_R_DZ span:nth-child(1)::text').extract()

            items['name'] = name
            items['actual_price'] = actual_price
            items['price_without_discount'] = price_without_discount
            items['discount'] = discount
            items['specification'] = specification
            items['rating'] = rating
            items['total_ratings'] = total_ratings

            yield items

        next_page = 'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Realme&p%5B%5D=facets.brand%255B%255D%3DPOCO&page='+str(Spider_mobile.page_number)

        if Spider_mobile.page_number<6:
            Spider_mobile.page_number += 1
            yield response.follow(next_page, callback=self.parse)