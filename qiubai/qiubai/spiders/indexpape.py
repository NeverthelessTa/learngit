import scrapy
class QiubaiSpider(scrapy.Spider):
      name='qiubai'
      start_urls=[
          "http://www.qiushibaike.com/",
      ]
      def parse(self, response):
          print(response.xpath('//div[@class="content"]/span').extract())