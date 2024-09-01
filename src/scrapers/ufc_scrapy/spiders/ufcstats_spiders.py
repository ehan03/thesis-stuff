# standard library imports

# third party imports
from scrapy.spiders import Spider

# local imports


class UFCStatsSpider(Spider):
    name = "ufcstats"
    allowed_domains = ["ufcstats.com"]
    start_urls = [
        "http://ufcstats.com/statistics/events/completed?page=all",
    ]
    custom_settings = {
        "ROBOTSTXT_OBEY": False,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 10,
        "CONCURRENT_REQUESTS": 10,
        "COOKIES_ENABLED": False,
        "DOWNLOADER_MIDDLEWARES": {
            "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
            "scrapy_user_agents.middlewares.RandomUserAgentMiddleware": 400,
        },
        "REQUEST_FINGERPRINTER_IMPLEMENTATION": "2.7",
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        "FEED_EXPORT_ENCODING": "utf-8",
        "DEPTH_PRIORITY": 1,
        "SCHEDULER_DISK_QUEUE": "scrapy.squeues.PickleFifoDiskQueue",
        "SCHEDULER_MEMORY_QUEUE": "scrapy.squeues.FifoMemoryQueue",
        "RETRY_TIMES": 0,
        "LOG_LEVEL": "INFO",
        "ITEM_PIPELINES": {
            "ufc_scrapy.scrapy_pipelines.ufcstats_pipelines.UFCStatsFightersPipeline": 100,
            "ufc_scrapy.scrapy_pipelines.ufcstats_pipelines.UFCStatsCompletedBoutsPipeline": 200,
        },
        "CLOSESPIDER_ERRORCOUNT": 1,
    }

    def parse(self, response):
        event_urls = ["http://ufcstats.com/event-details/6420efac0578988b"]
        event_urls.extend(
            reversed(
                response.css(
                    """tr.b-statistics__table-row >
                td.b-statistics__table-col >
                i.b-statistics__table-content >
                a.b-link.b-link_style_black::attr(href)"""
                ).getall()
            )
        )

    def parse_event(self, response):
        pass
