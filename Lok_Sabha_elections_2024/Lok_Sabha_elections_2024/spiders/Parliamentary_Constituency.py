import scrapy
import logging


class ParliamentaryConstituencySpider(scrapy.Spider):
    name = "Parliamentary_Constituency"
    allowed_domains = ["results.eci.gov.in"]
    start_urls = ["https://results.eci.gov.in/PcResultGenJune2024/index.htm"]

    def parse(self, response):
        party_names = response.xpath("//table/tbody/tr/td[1]/text()").getall()
        seats_won = response.xpath("//table/tbody/tr/td[2]/a")
        for candidate in seats_won:
            link = candidate.xpath(".//@href").get()
            yield response.follow(url=link, callback=self.parse_candidate)

            
    def parse_candidate(self,response):
        rows = response.xpath("(//table[@class='table table-striped table-bordered'])[1]/tbody/tr")
        for row in rows:
            parliament_constituency = row.xpath(".//td[2]/a/text()").get()
            winning_candidate = row.xpath(".//td[3]/text()").get()
            total_votes = row.xpath(".//td[4]/text()").get()
            margin = row.xpath(".//td[5]/text()").get()

            yield{
                'parliament constituency' : parliament_constituency,
                'winning candidate' : winning_candidate,
                'total votes' : total_votes,
                'Margin' : margin
            }

