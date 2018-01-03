# -*- coding: utf-8 -*-
import scrapy
import json
from Courses.items import  CoursesItem


class CoursesSpiderSpider(scrapy.Spider):
    name = 'course_spider'
    allowed_domains = ['study.163.com']

    def start_requests(self):
        req = []
        page_size = 500
        for page_index in range(0, int(5000 / page_size)):
            post_data = json.dumps(
                {"pageIndex": page_index, "pageSize": page_size, "relativeOffset": page_size * (page_index - 1),
                 "frontCategoryId": -1, "searchTimeType": -1, "orderType": 0, "priceType": -1, "activityId": 0})
            json_api_url = 'http://study.163.com/p/search/studycourse.json'
            requests = req.append(scrapy.Request(json_api_url, method='POST', body=post_data, callback=self.parse,
                                                 meta={'proxy': 'http://localhost:8888'}))
        return req

    def parse(self, response):
        respose_info = json.loads(response.body)
        item = CoursesItem()
        item['result_list'] = respose_info['result']['list']
        return item