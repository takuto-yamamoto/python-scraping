from datetime import datetime
from string import whitespace


class WikiSpiderPipeline(object):
    def process_item(self, article, spider):
        article["last_updated"] = article["last_updated"].replace(
            "This page was last edited on", ""
        )
        article["last_updated"] = article["last_updated"].strip()
        article["last_updated"] = datetime.strptime(
            article["last_updated"], "%d %B %Y, at %H:%M"
        )
        article["text"] = [
            line for line in article["text"] if line not in whitespace
        ]
        article["text"] = "".join(article["text"])
        return article
