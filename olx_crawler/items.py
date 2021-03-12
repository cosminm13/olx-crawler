# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OlxItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    user = scrapy.Field()
    location = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()
    owner_type = scrapy.Field()
    brand = scrapy.Field()
    model = scrapy.Field()
    color = scrapy.Field()
    fuel_type = scrapy.Field()
    gearbox_type = scrapy.Field()
    year = scrapy.Field()
    mileage = scrapy.Field()
    body_type = scrapy.Field()
    engine_displacement = scrapy.Field()
    condition = scrapy.Field()
    post_date = scrapy.Field()
    views = scrapy.Field()

