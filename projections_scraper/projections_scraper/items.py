# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class QBProjectionsItem(Item):
    name = Field()
    pa_att = Field()
    pa_cmp = Field()
    pa_yds = Field()
    pa_tds = Field()
    ints = Field()
    ru_att = Field()
    ru_yds = Field()
    ru_tds = Field()
    fl = Field()
    fpts = Field()

class RBProjectionsItem(Item):
    name = Field()
    ru_att = Field()
    ru_yds = Field()
    ru_tds = Field()
    rec = Field()
    rec_yds = Field()
    rec_tds = Field()
    fl = Field()
    fpts = Field()
