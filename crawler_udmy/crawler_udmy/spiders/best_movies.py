import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'imdb250'
    allowed_domains = ['imdb.com']
    # Old Url: http://web.archive.org/web/20200715000935if_/https://www.imdb.com/search/title/?groups=top_250&sort=user_rating
    start_urls = ['https://www.imdb.com/search/title/?groups=top_250&sort=user_rating']

    rules = (  # Rule order matters, be careful!
        Rule(
            LinkExtractor(
                restrict_xpaths=("//*[@class='lister-item-content']/h3/a", )),  # can have multiple xpath items
                callback='parse_item', follow=True),
        Rule(
            LinkExtractor(  # since we don't have a callback method (because it remembers it from the previous Rule), we don't need to specify 'follow' argument. It's True by default.
                restrict_xpaths='//*[@class="lister-page-next next-page"]'))  # if only 1 item, don't have to use a tuple as above
    )

    def parse_item(self, response):
        title = response.xpath('//*[@class="TitleBlock__Container-sc-1nlhx7j-0 hglRHk"]/div/h1/text()').get()
        year = response.xpath('//*[@class="TitleBlock__Container-sc-1nlhx7j-0 hglRHk"]/div/div/ul/li/span[1]/text()').get()
        duration = response.xpath('//*[@class="TitleBlock__Container-sc-1nlhx7j-0 hglRHk"]/div/div/ul/li[3]/text()').get()
        genre = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/div/a/span/text()').get()
        rating = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[2]/div/div[1]/a/div/div/div[2]/div[1]/span[1]/text()').get()
        movie_url = response.url
        yield {
            "title": title,
            "year": year,
            "duration": duration,
            "genre": genre,
            "rating": rating,
            "movie_url": movie_url,
        }