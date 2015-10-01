from scrapy.spider import Spider
from scrapy.selector import Selector
from projections_scraper.items import QBProjectionsItem, RBProjectionsItem

class QBProjectionsSpider(Spider):

    name = 'fantasypros.com'
    allowed_domains = ['fantasypros.com']
    start_urls = ['http://www.fantasypros.com/nfl/projections/qb.php']

    def parse(self, response):

        rows = response.xpath("//div[@class='mobile-table']//table/tbody/tr")

        data = QBProjectionsItem()

        for row in rows:
            data = QBProjectionsItem()
            data['name'] = row.xpath("td/a/text()").extract()
            data['pa_att'] = row.xpath("td[2]/text()").extract()
            data['pa_cmp'] = row.xpath("td[3]/text()").extract()
            data['pa_yds'] = row.xpath("td[4]/text()").extract()
            data['pa_tds'] = row.xpath("td[5]/text()").extract()
            data['ints'] = row.xpath("td[6]/text()").extract()
            data['ru_att'] = row.xpath("td[7]/text()").extract()
            data['ru_yds'] = row.xpath("td[8]/text()").extract()
            data['ru_tds'] = row.xpath("td[9]/text()").extract()
            data['fl'] = row.xpath("td[10]/text()").extract()
            data['fpts'] = row.xpath("td[11]/text()").extract()

            yield data

# class RBProjectionsSpider(Spider):
#
#     name = 'fantasypros.com'
#     allowed_domains = ['fantasypros.com']
#     start_urls = ['http://www.fantasypros.com/nfl/projections/rb.php']
#
#     def parse(self, response):
#
#         rows = response.xpath("//div[@class='mobile-table']//table/tbody/tr")
#
#         data = RBProjectionsItem()
#
#         for row in rows:
#             data = RBProjectionsItem()
#             data['name'] = row.xpath("td/a/text()").extract()
#             data['ru_att'] = row.xpath("td[2]/text()").extract()
#             data['ru_yds'] = row.xpath("td[4]/text()").extract()
#             data['ru_tds'] = row.xpath("td[5]/text()").extract()
#             data['rec'] = row.xpath("td[6]/text()").extract()
#             data['rec_yds'] = row.xpath("td[7]/text()").extract()
#             data['rec_tds'] = row.xpath("td[9]/text()").extract()
#             data['fl'] = row.xpath("td[10]/text()").extract()
#             data['fpts'] = row.xpath("td[11]/text()").extract()
#
#             yield data
