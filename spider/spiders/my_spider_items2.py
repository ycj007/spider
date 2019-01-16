from logging import info

import scrapy


class itemSpider(scrapy.Spider):
    name = 'my_spider_items2'
    start_urls = ['http://lab.scrapyd.cn']

    def parse(self, response):
        mingyan = response.css('div.quote')

        for v in mingyan:
            text = v.css('.text::text').extract_first()
            author = v.css('.author::text').extract_first()
            tags = v.css('.tags .tag::text').extract_first()
            if not tags:
                tags=[]
            if not author:
                    author = ""
            tags = ",".join(tags)



            filename="%s-语录.txt" % author

            with open(filename,"a+") as f:
                f.write(text)
                f.write("\n")
                f.write("标签："+tags)
                f.write("\n")
                f.write(100*"-")
                f.write("\n")
                f.close()
        next_page = response.css('li.next a::attr(href)').extract_first()
        info(next_page)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)



