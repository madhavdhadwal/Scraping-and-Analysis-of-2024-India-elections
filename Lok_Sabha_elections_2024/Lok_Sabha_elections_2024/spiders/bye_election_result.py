import scrapy

class ByeElectionResultSpider(scrapy.Spider):
    name = "bye_election_result"
    allowed_domains = ["results.eci.gov.in"]
    start_urls = ["https://results.eci.gov.in/AcResultByeJune2024/index.htm"]

    def parse(self, response):
        boxes = response.xpath("//div[contains(@class, 'const-box')]")
        for box in boxes:
            constituency = box.xpath(".//h3/text()").get()
            state = box.xpath(".//h4/text()").get()
            winning_party = box.xpath(".//h6/text()").get()

            yield {
                'Constituency': constituency,
                'State': state,
                'Winning Party': winning_party
            }
