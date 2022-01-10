import scrapy
import json

class WagesProvincesSpider(scrapy.Spider):

    name = "provinces_wages"
    start_urls = [
        'https://pc.saiteichingin.info/table/page_list_nationallist.php'
    ]

    def parse(self, response):

        self.region_name = ''
        self.result = {}
        self.province_data = {}

        for tr in response.xpath(f'//div[contains(@class,"industryTableArea_list")]/table/tbody/tr'):
            if tr.xpath(f'./th[contains(@class,"area")]/span/text()'): # pega o nome da região
                
                self.region_name = tr.xpath(f'./th[contains(@class,"area")]/span/text()').extract()
            
            elif self.region_name :# adiciona mais um valor ao dicionário formado pelas regiões + suas provincias
                
                self.province_data['province name'] = tr.xpath(f'./td/a/text()').extract()
                self.province_data['wage'] = tr.xpath(f'./td[contains(@class,"money")]/text()').extract()
                self.province_data['date'] = tr.xpath(f'./td[contains(@class,"date")]/text()').extract()
                
                if f'{self.region_name}' in self.result: # caso ainda não exista uma chave no dicionário com o nome da região, cria ela, pois se tentar dar o append direto, ele dá erro de chave inexistente
                    self.result[f'{self.region_name}'].append(f'{self.province_data}')
                else:
                    self.result[f'{self.region_name}'] = [f'{self.province_data}']

        self.log(self.result)
        with open('test.txt','wb') as file:
            file.write(json.dumps(self.result, ensure_ascii=False).encode('utf8'))