# -*- coding: utf-8 -*-
BOT_NAME = "wikiSpider"

SPIDER_MODULES = ["wikiSpider.spiders"]
NEWSPIDER_MODULE = "wikiSpider.spiders"
ITEM_PIPELINES = {
    "wikiSpider.pipelines.WikiSpiderPipeline": 300,
}

ROBOTSTXT_OBEY = True

# LOG_LEVEL = "ERROR"
