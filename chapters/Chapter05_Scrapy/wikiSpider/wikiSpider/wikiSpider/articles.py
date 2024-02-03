import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ArticleSpider(CrawlSpider):
    name = "articles"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Benevolent_dictator_for_life"]
    rules = [
        Rule(
            LinkExtractor(allow="^(/wiki/)((?!:).)*$"),
            callback="parse_items",
            cb_kwargs={"is_article": True},
            follow=True,
        ),
        Rule(
            LinkExtractor(allow=".*"),
            callback="parse_items",
            cb_kwargs={"is_article": False},
            follow=False,
        ),
    ]

    def parse_items(self, response: scrapy.http.Response, is_article: bool):
        url = response.url
        title = response.css("h1 span::text").extract_first()

        if ~is_article:
            print(f"URL is {url}")
            print(f"This is not an article: {title}")

        text = response.xpath('//div[@id="mw-content-text"]//text()').extract()
        last_updated = response.css(
            "li#footer-info-lastmod::text"
        ).extract_first()
        last_updated = (
            last_updated.replace("This page was last edited on ", "")
            if last_updated
            else "Not available"
        )

        print(f"URL is {url}")
        print(f"title is {title}")
        print(f"text is {text}")
        print(f"last updated: {last_updated}")
