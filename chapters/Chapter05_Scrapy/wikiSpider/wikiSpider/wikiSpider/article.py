import scrapy


class ArticleSpider(scrapy.Spider):
    name = "article"
    start_urls = [
        "http://en.wikipedia.org/wiki/Python_%28programming_language%29",
        "https://en.wikipedia.org/wiki/Functional_programming",
        "https://en.wikipedia.org/wiki/Monty_Python",
    ]

    def parse(self, response):
        url = response.url
        title = response.css("h1 span::text").extract_first()
        print(f"URL is: {url}")
        print(f"Title is {title}")
