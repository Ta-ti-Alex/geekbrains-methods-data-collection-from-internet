# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from itemloaders.processors import MapCompose, Compose, TakeFirst

def process_price(price):
    price = price[0].replace("\xa0", " ")
    try:
        price = price.split()[0]
        price = int(price)
    except Exception as e:
        print(e)
        pass
    return price


def process_photo(photo):
    print()
    if photo.startswith('//'):
        photo = "https:" + photo.split()[0]
    else:
        photo = photo.split()[1]
    return photo

class AvitoparserItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(input_processor=Compose(process_price), output_processor=TakeFirst())
    author = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field(input_processor=MapCompose(process_photo))
    url = scrapy.Field(output_processor=TakeFirst())



#class AvitoparserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
