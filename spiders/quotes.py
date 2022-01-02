import scrapy
from ..items import SeamsfriendlyItem


class quotespider(scrapy.Spider):
    page_number = 2
    name = "quotes"
    start_urls = [
        "https://in.seamsfriendly.com/collections/shorts/?page=1"
    ]

    def parse(self, response):

        item_grid = response.css('div.Grid__Cell')

        for grid in item_grid:
            product_title = grid.css("h2.ProductItem__Title a::text").extract()
            image_url = grid.css("img.ProductItem__Image").xpath("@src").extract()
            price = grid.css("span.ProductItem__Price::text").extract()
            description = grid.css("div.label_icon::text").extract()


            item = SeamsfriendlyItem()

            item['product_title'] = product_title
            item['image_url'] =image_url
            item['price'] = price
            item['description'] = description




            yield item



        next_page="https://in.seamsfriendly.com/collections/shorts/?page=" + str(quotespider.page_number) + '/'

        if quotespider.page_number<=3:
            quotespider.page_number +=1
            yield response.follow(next_page,callback=self.parse)