import scrapy


class AssemblyConstituencyGeneralAndhraSpider(scrapy.Spider):
    name = "Assembly_constituency_general_Andhra"
    allowed_domains = ["results.eci.gov.in"]
    start_urls = ["https://results.eci.gov.in/AcResultGenJune2024/statewiseS011.htm"]

    def parse(self, response):
        rows = response.xpath("(//table[@class='table table-striped table-bordered'])[1]/tbody/tr")
        for row in rows:
            Constituency = row.xpath(".//td[1]/text()").get()
            Leading_party = row.xpath(".//td[4]//tr/td[1]/text()").get()
            Trailing_party = row.xpath(".//td[6]//tr/td[1]/text()").get()
            Margin = row.xpath(".//td[7]/text()").get()

            yield {
                'Constituency': Constituency,
                'Leading Party': Leading_party,
                'Trailing Party': Trailing_party,
                'Margin': Margin
            }

        page_links = response.xpath("//a[@class='page-link']/@href").getall()
        
        for link in page_links:
            if link:
                next_page_url = response.urljoin(link)
                yield scrapy.Request(next_page_url, callback=self.parse)
