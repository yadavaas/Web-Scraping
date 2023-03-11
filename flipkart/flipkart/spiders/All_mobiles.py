import scrapy
from ..items import FlipkartItem

class Spider_mobile(scrapy.Spider):
    name = 'all_mobile_scrap'
    start_urls = ['https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3Drealme&otracker=nmenu_sub_Electronics_0_Realme&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DAPPLE&p%5B%5D=facets.brand%255B%255D%3DGoogle&p%5B%5D=facets.brand%255B%255D%3DHonor&p%5B%5D=facets.brand%255B%255D%3DHTC&p%5B%5D=facets.brand%255B%255D%3DNokia&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3Doppo&p%5B%5D=facets.brand%255B%255D%3DOPPO&p%5B%5D=facets.brand%255B%255D%3DREDMI&p%5B%5D=facets.brand%255B%255D%3DSONY&p%5B%5D=facets.brand%255B%255D%3DSony%2BEricsson&p%5B%5D=facets.brand%255B%255D%3DVIVO&p%5B%5D=facets.brand%255B%255D%3DVivo&p%5B%5D=facets.brand%255B%255D%3Dvivo&p%5B%5D=facets.brand%255B%255D%3DCelkon&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.brand%255B%255D%3DPOCO']
    # page_number = 2

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

        # next_page = 'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3Drealme&otracker=nmenu_sub_Electronics_0_Realme&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DAPPLE&p%5B%5D=facets.brand%255B%255D%3DGoogle&p%5B%5D=facets.brand%255B%255D%3DHonor&p%5B%5D=facets.brand%255B%255D%3DHTC&p%5B%5D=facets.brand%255B%255D%3DNokia&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3Doppo&p%5B%5D=facets.brand%255B%255D%3DOPPO&p%5B%5D=facets.brand%255B%255D%3DREDMI&p%5B%5D=facets.brand%255B%255D%3DSONY&p%5B%5D=facets.brand%255B%255D%3DSony%2BEricsson&p%5B%5D=facets.brand%255B%255D%3DVIVO&p%5B%5D=facets.brand%255B%255D%3DVivo&p%5B%5D=facets.brand%255B%255D%3Dvivo&p%5B%5D=facets.brand%255B%255D%3DCelkon&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.brand%255B%255D%3DPOCO&page=2'+str(Spider_mobile.page_number)
        #
        # if Spider_mobile.page_number<120:
        #     Spider_mobile.page_number+= 1
        #     yield response.follow(next_page, callback=self.parse)

        next_page = response.css('a._1LKTO3::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)