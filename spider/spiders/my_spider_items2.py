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



