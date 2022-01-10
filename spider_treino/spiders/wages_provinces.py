import scrapy


class WagesProvincesSpider(scrapy.Spider):

    name = "provinces_wages"
    start_urls = [
        'https://pc.saiteichingin.info/table/page_list_nationallist.php'
    ]

    def parse(self, response):
        tags = response.xpath('//div[contains(@class,"industryTableArea_list")]/table/tbody/tr/th[contains(@class,"area")]/span/text()'
        ).extract()
        self.log(tags)