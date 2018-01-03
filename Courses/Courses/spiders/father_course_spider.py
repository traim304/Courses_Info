# -*- coding: utf-8 -*-
import scrapy
import json
from Courses.items import  CoursesItem



class FatherCourseSpiderSpider(scrapy.Spider):
    name = 'father_course_spider'
    allowed_domains = ['study.163.com']

    def start_requests(self):
        post_data = json.dumps({"pageIndex":1,"pageSize":500,"relativeOffset":0,"frontCategoryId":-1,
                                "searchTimeType":-1,"orderType":0,"priceType":-1,"activityId":0})
        json_api_url = 'http://study.163.com/p/search/studycourse.json'
        return [scrapy.Request(json_api_url, method='POST', body=post_data, callback=self.parse,
                               meta={'proxy': 'http://localhost:8888'}),]

    def parse(self, response):
        respose_info = json.loads(response.body)
        item = CoursesItem()
        item['result_list'] = respose_info['result']['list']
        return item