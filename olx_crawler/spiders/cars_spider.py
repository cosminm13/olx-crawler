import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from olx_crawler.items import OlxItem


class CarsSpider(CrawlSpider):
    name = "cars"
    allowed_domains = ["www.olx.ro"]
    start_urls = open('links.txt').readlines()

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        item_links = response.css('table .wrap .offer h3 a::attr(href)').extract()
        for a in item_links:
            yield scrapy.Request(a, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        id = response.css('.offer-bottombar__item > strong::text').get()
        title = response.css('h1::text').get().strip()
        price = response.css('.pricelabel > strong::text').get()
        user = response.css('.offer-user__actions h4 a::attr(href)').get()
        location = response.css('address p::text').get()

        # properties
        properties = response.css('.offer-details__name *::text').getall()
        values = response.css('.offer-details__value *::text').getall()
        for i, p in enumerate(properties):
            if p == 'Oferit de':
                owner_type = values[i]
            elif p == 'Marca':
                brand = values[i]
            elif p == 'Model':
                model = values[i]
            elif p == 'Culoare':
                color = values[i]
            elif p == 'Combustibil':
                fuel_type = values[i]
            elif p == 'Cutie de viteze':
                gearbox_type = values[i]
            elif p == 'An de fabricatie':
                year = values[i]
            elif p == 'Rulaj':
                mileage = values[i]
            elif p == 'Caroserie':
                body_type = values[i]
            elif p == 'Capacitate motor':
                engine_displacement = values[i]
            elif p == 'Stare':
                condition = values[i]

        description = response.xpath('.//div[@id="textContent"]/text()').getall()
        # description = [i.strip() + '\n' for i in list(response.xpath('.//div[@id="textContent"]/text()').getall())]
        post_date = response.css('em > strong::text').get()[3:]
        views = response.css('.offer-bottombar__counter > strong::text').get()

        item = OlxItem()
        item['id'] = id
        item['title'] = title
        item['price'] = price
        item['user'] = user
        item['url'] = response.url
        item['location'] = location
        item['description'] = description

        item['owner_type'] = owner_type
        item['brand'] = brand
        item['model'] = model
        item['color'] = color
        item['fuel_type'] = fuel_type
        item['gearbox_type'] = gearbox_type
        item['year'] = year
        item['mileage'] = mileage
        item['body_type'] = body_type
        item['engine_displacement'] = engine_displacement
        item['condition'] = condition

        item['post_date'] = post_date
        item['views'] = views
        yield item
