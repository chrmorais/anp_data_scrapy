from scrapy.item import Item, Field

class ANPItem(Item):
    id = Field()
    name = Field()
    fantasy_name = Field()
    address = Field()
    additional_address = Field()
    district = Field()
    city_state = Field()  # TODO split this latter
    zipcode = Field()
    number_dispacth = Field()
    date = Field()
    type = Field()
