import scrapy

class Overall_Result(scrapy.Spider):
    name = "Overall_Result"
    allowed_domains = ["results.eci.gov.in"]
    start_urls = ["https://results.eci.gov.in/PcResultGenJune2024/index.htm"]

    def parse(self, response):
        rows = response.xpath("(//table[@class='table'])[1]/tbody/tr")
        for row in rows:
            party_names = row.xpath(".//td[1]/text()").get()
            seats_won = row.xpath(".//td[2]/a/text()").get()

            yield {
                'Party name': party_names,
                'Seats won': seats_won
            }
