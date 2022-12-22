import  scrapy

class PrecoMotosSpider(scrapy.Spider):
 
    name= 'precobot'

    def start_requests(self):
        urls = ["https://www.honda.com.br/motos/modelos"]

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse,meta={'next_url':urls[0]})


    def parse(self, response):
        for moto in response.xpath("//div[@class='single-product-container']"):
            yield {
                'modelo': moto.xpath(".//h3[@class='title']/a/text()").get(),
                'preco': moto.xpath(".//span[@class='price']/text()").get(),
                'link': moto.xpath(".//h3[@class='title']/a/@href").get(),
            }