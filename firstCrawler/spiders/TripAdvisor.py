import scrapy as lol
from firstCrawler.items import TripAdvisorItems

class TripAdvisor(lol.Spider):
#Defining Name of Spider
    name='tripadvisor'
#Domains allowed during scrape session | Outer domains will be filtered
    allowed_domain=[
        'tripadvisor.com'
                    ]

#Start URLS for scraping
    start_urls=[
        'https://www.tripadvisor.in/Restaurants-g297628-Bengaluru_Karnataka.html'
            ]

#Parse function default call here
    def parse(self,response):
        #Parse data from Start url and  use each url to fetch restaurant data
        urls=response.xpath("//h3[@class='title']/a/@href").extract()
        print(urls)
        #New request is created for each URL fetched and it is parsed using diff function
        #absolute_urls contain restaurant data
        for url in urls:
            #Change it to absolute url
            absolute_urls=response.urljoin(url)
            #make a new Scrapy Request but handle it using different parser as diff HTML doc.
            yield lol.Request(absolute_urls,callback=self.parse_restaurent_data)

        #Now switching page for next request (Relative one)
            next_page_url = response.xpath("// a[text()='Next']/@href").extract_first()
        #Change it to absolute URL
            next_absolute_urls=response.urljoin(next_page_url)
        #Now call this next url and it will be parsed by default parser
            yield lol.Request(next_absolute_urls,callback=self.parse)

    def parse_restaurent_data(self,response):
        print('Finally inside artificial parser')
        #fetching info from extracted pages
        name=response.xpath('//div[@class="mapContainer"]/@data-name').extract_first()
        ratings = response.xpath('//img[@property="ratingValue"]/@content').extract_first()
        latitude = response.xpath('//div[@class="mapContainer"]/@data-lng').extract_first()
        longitude = response.xpath('//div[@class="mapContainer"]/@data-locid').extract_first()
        url=response.url

        #Store these items into Items Class
        item=TripAdvisorItems()

        item['name']=name
        item['rating'] = ratings
        item['latitude'] = latitude
        item['longitude'] = longitude
        item['url'] = url

        #Yield all output so that it can be later filled into output stream
        yield item
