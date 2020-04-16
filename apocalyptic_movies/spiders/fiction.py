import scrapy
import string
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

class Fiction(scrapy.Spider):
    name = 'fiction'

    start_urls = ['https://en.wikipedia.org/wiki/List_of_apocalyptic_and_post-apocalyptic_fiction']

    def parse(self, response):
        table = response.xpath('//*[@id="mw-content-text"]/div/table[2]//tbody')
        rows = table.xpath('//tr')
        for row in rows:
            try:
                format_ = row.xpath('td//text()')[0].extract()
                date = row.xpath('td//text()')[1].extract()
                if not hasNumbers(date):
                    continue
                genre = row.xpath('td//text()')[2].extract()
                title = row.css('td')[3].xpath('normalize-space()').extract_first()
            except: 
                continue
            yield {'format': format_,
                    'date': date,
                    'genre': genre,
                    'title': title}
                    
