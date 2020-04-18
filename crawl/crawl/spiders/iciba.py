# -*- coding: utf-8 -*-
import scrapy
from crawl.items import WordItem


class IcibaSpider(scrapy.Spider):
    name = 'iciba'
    allowed_domains = ['word.iciba.com']
    start_urls = ['http://word.iciba.com/?action=words&class=11&course=1']

    def parse(self, response):
        for li in response.xpath('//ul/li'):
            word = li.xpath('./div[1]/span/text()').extract()
            translate = li.xpath('./div[3]/span/text()').extract()
            pronunciation = li.xpath('./div[2]/strong/text()').extract()
            mp3_link = li.xpath('./div[2]/a/@id').extract()
            page = response.xpath("//form/input[@name='course_id']/@value").extract()[0]
            word_item = WordItem()
            word_item['word'] = self.trim(word)
            word_item['pronunciation'] = self.trim(pronunciation)
            word_item['translate'] = self.trim(translate)
            word_item['mp3_link'] = self.trim(mp3_link)
            word_item['current_page'] = page
            yield word_item
        page = int(page)+1
        print(page)
        url = 'http://word.iciba.com/?action=words&class=11&course=' + str(page)
        if page == 227 : return
        yield scrapy.Request(url,callback=self.parse)

    @staticmethod
    def trim(text):
        if type(text) != str:
            return "".join(text[0].split())
        return "".join(text.split())