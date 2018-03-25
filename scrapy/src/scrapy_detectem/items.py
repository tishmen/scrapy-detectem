from scrapy import Field, Item
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Identity


class DetectemItem(Item):

    url = Field()
    data = Field()
    timestamp = Field()


class DetectemLoader(ItemLoader):

    default_item_class = DetectemItem
    default_output_processor = TakeFirst()
    data_out = Identity()
