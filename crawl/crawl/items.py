# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WordItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    word = scrapy.Field()
    pronunciation = scrapy.Field()
    translate = scrapy.Field()
    mp3_link = scrapy.Field()
    current_page = scrapy.Field()


