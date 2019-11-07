# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from os import path
from scrapy.exporters import CsvItemExporter

class CsvExportPipeline(object):
    def open_spider(self, spider):
        csv_path = path.join(path.dirname(__file__),'../data')
        self.file = open(path.join(csv_path, 'legislativeElectionResults.csv'), 'wb+')
        # TODO fields to export
        self.export = CsvItemExporter(
            file=self.file
        )

    def close_spider(self, spider):
        self.export.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.export.export_item(item)
        return item