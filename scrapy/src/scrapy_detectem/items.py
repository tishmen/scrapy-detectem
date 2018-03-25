'''items.py'''

from scrapy import Field, Item
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Identity


class DetectemItem(Item):

    '''Detectem item.'''

    url = Field()
    data = Field()
    timestamp = Field()


class DetectemLoader(ItemLoader):

    '''Detectem item loader.'''

    default_item_class = DetectemItem
    default_output_processor = TakeFirst()
    data_out = Identity()
