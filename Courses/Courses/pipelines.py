# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import  settings
from pymongo.errors import  DuplicateKeyError

class CoursesPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host, port=port)
        tdb = client[dbname]
        self.post = tdb[settings['MONGODB_DOCNAME']]


    def process_item(self, item, spider):
        for info in item['result_list']:
            info['_id'] = info['courseId']
            try:
                self.post.insert(info)
            except DuplicateKeyError:
                pass
        return item
