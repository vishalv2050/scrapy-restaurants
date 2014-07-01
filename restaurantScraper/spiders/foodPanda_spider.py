import scrapy
import re

from tutorial.items import MenuItem

class DmozSpider(scrapy.Spider):
    name = "justeat"
    allowed_domains = ["foodpanda.in"]
    start_urls = [
        "http://justeat.in/noida/wah-ji-wah-sector-27-10760/menu",
        "http://justeat.in/noida/restaurants/sector-25",
    ]

    

    # def parse(self, response):
    # 	regex = re.compile('Rs\.([0-9.]*)\.[0-9]*')
    #     for sel in response.xpath('//div[@class="menu-product clearfix no-variation"]'):
    #     	name = sel.xpath('div[1]/text()').extract();
    #     	price = sel.xpath('div[3]/text()').extract();

    #     	name = ''.join(name).strip()
    #     	price = ''.join(price)
    #     	price = price.strip()
    #     	itemPrice = 0

    #     	match = regex.match(price)
    #     	if match:
    #     		itemPrice = int(match.group(1))

    #     	item = MenuItem()
    #     	item['name'] = name;
    #     	item['price'] = itemPrice;

    #     	yield item


    def parse(self, response):
        menuUrl = re.compile('[0-9A-Fa-f]*menu')

        startUrl = re.compile('')

    	regex = re.compile('Rs\.([0-9.]*)\.[0-9]*')

    	resp = response.xpath('//div[@class="restInfoDetails"]')[0]
    	resp = resp.xpath('h1/text()')

    	restName = resp.extract()
    	restName = ''.join(restName)
    	restName = restName.strip()
        if menuUrl.match(response.url):
            for sel in response.xpath('//tr[@class="prdLi1"]'):
            	name = sel.xpath('td[1]/span/text()').extract();
            	price = sel.xpath('td[5]/span/text()').extract();

            	name = ''.join(name).strip()
            	price = ''.join(price).strip()

            	print price;

            	try:
    	        	itemPrice = int(price)

    	        	item = MenuItem()
    	        	item['name'] = name;
    	        	item['price'] = price;
    	        	item['restName'] = restName;
    	        	yield item
    	        except ValueError:
    	        	print 'Failed'

        	


