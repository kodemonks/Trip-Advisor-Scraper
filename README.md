# TripAdvisorScraper
Sample Scraper that scrpes TripAdvisor for Restaurents in Bangalore area

## How to run
### scrapy crawl tripadvisor -o output.csv -t csv

  tripadvisor - Name of Crawler [can be changed from name attribute in TripAdvisor.py]
  -o specify Output type
  -t File type

##start_urls
Can be modified for different Area urls https://www.tripadvisor.in/Restaurants-g297628-Bengaluru_Karnataka.html

##Output - 
  Output will be stored in output.csv (Can be changed while running crawler command)
###RestaurentName | URL | Ratings | Latitude | Longtitude
