# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FlipkartItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    actual_price = scrapy.Field()
    price_without_discount = scrapy.Field()
    discount = scrapy.Field()
    rating = scrapy.Field()
    total_ratings = scrapy.Field()
    specification = scrapy.Field()
