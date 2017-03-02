from scrapy.item import Item,Field


#Item Class to store Data
class TripAdvisorItems(Item):
    name=Field()
    rating=Field()
    latitude=Field()
    longitude=Field()
    url=Field()
