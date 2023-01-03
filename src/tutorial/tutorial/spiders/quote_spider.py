import scrapy

class QuotesSpider(scrapy.Spider):
    # 크롤링 함수의 이름
    name = "quotes"

    # 요청(Request)보낼 URL 리스트
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            # yield: 함수의 실행을 중단하고, 호출한 곳으로 돌아간다.
            yield scrapy.Request(url=url, callback=self.parse)


    # Response를 받아서 처리하는 함수
    def parse(self, response):
        quote = response.css('div.quote')
        print(quote)
        # page = response.url.split("/")[-2]
        # saveDir = 'results/'
        # filename = saveDir + 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
