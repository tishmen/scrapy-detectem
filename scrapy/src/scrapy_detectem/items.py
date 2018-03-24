from scrapy import Field, Item
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Identity


class DetectemItem(object):

    url = Field()
    data = Field()


class DetectemLoader(ItemLoader):

    default_item_class = DetectemItem
    url_out = TakeFirst()
    data_out = Identity()
