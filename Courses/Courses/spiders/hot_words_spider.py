# -*- coding: utf-8 -*-
import scrapy
import os
from scrapy.shell import inspect_response


class HotWordsSpiderSpider(scrapy.Spider):
    name = 'hot_words_spider'
    allowed_domains = ['study.163.com']

    def start_requests(self):
        reqs = []
        for i in range(4):
            start_url = 'http://study.163.com/j/search/hotwords.json?hotwordType=' + str(i)
            reqs.append(scrapy.Request(start_url, meta={'proxy': 'localhost:8888'}, callback=self.parse))
        return reqs

    def parse(self, response):
        # inspect_response(response,self)
        import json
        hot_key = json.loads(response.body)['result']
        with open('./hotwords.txt', 'a') as f:
            for word in hot_key:
                f.write(word)
                f.write('\n')
