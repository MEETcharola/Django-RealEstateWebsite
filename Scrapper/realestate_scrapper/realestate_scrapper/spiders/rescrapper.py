import urllib
import scrapy
from cssselect import Selector
from realestate_scrapper.items import RealestateScrapperItem


class Real_Estate(scrapy.Spider):
    name = "RE"
    start_urls = [
        "https://www.nobroker.in/property/sale/mumbai/Borivali%20West?type=BHK3&searchParam=W3sibGF0IjoxOS4yMzgwNjgzLCJsb24iOjcyLjg1MjI1MTIsInBsYWNlSWQiOiJDaElKOXhmUlBNNnc1enNSa3ZaYmxZdFZYVkUiLCJwbGFjZU5hbWUiOiJCb3JpdmFsaSBXZXN0In1d&radius=2.0"]

    def parse(self, response):
        properties_url = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "nb__1AShY", " " ))]/../@href').getall()
        print("TOTAL PROPERTIES IN THIS PAGE : ", end="")
        print(len(properties_url))
        for p_url in properties_url:
            property = {}
            re_property_id = p_url.split('/')[-2]
            property['re_property_id'] = re_property_id
            yield response.follow(p_url, self.parse_property, meta={'property': property})

    def parse_property(self, response):
        item = RealestateScrapperItem()

        property = response.meta['property']
        title = response.css('.nb__s_YQN::text').extract_first()
        address = response.css('.nb__16pur::text').extract_first()
        city = response.css('.nb__2n7NV a:nth-child(2)::text').extract_first()
        locality = response.css('.nb__2n7NV a:nth-child(3)::text').extract_first()
        description = response.css('#description::text').extract_first()
        price = response.css('.nb__3h7Fo span::text').extract()
        bedrooms = response.css('.nb__3Z_gh:nth-child(1) .nb__GDnvX::text').extract_first()
        bathrooms = response.css('.nb__3Z_gh:nth-child(3) .nb__GDnvX::text').extract_first()
        balconies = response.css('.nb__3Z_gh:nth-child(5) .nb__GDnvX::text').extract_first()
        floor_number = response.css('.nb__3ocPe:nth-child(9) .font-semi-bold::text').extract_first().split('/')[0]
        total_floor = floor_number.split('/')[1] if len(floor_number.split('/')) == 2 else floor_number
        carpet_area = response.css('.nb__3ocPe:nth-child(5) .font-semi-bold::text').extract_first()
        super_area = response.css('.nb__3ocPe:nth-child(6) .font-semi-bold::text').extract_first()
        furnishing = response.css('nb__3ocPe:nth-child(7) .font-semi-bold::text').extract_first()
        car_parking = response.css('.nb__3Z_gh:nth-child(7) .nb__GDnvX::text').extract_first()
        status = response.css('.nb__3Z_gh:nth-child(4) .nb__GDnvX::text').extract_first()
        date_posted = response.css('.nb__3Z_gh:nth-child(2) .nb__GDnvX::text').extract()

        property['title'] = title
        property['address'] = address
        property['city'] = city
        property['locality'] = locality
        property['description'] = description
        property['price'] = ' '.join([str(elem) for elem in price])
        property['bedrooms'] = bedrooms
        property['bathrooms'] = bathrooms
        property['balconies'] = balconies
        if floor_number in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            property['floor_number'] = floor_number
            property['total_floor'] = total_floor
        else:
            property['floor_number'] = 0
            property['total_floor'] = 0
        property['carpet_area'] = carpet_area
        if super_area == "Fully furnished" or super_area == "Semi" :
            property['super_area'] = "NA"
            property['furnishing'] = super_area
        else:
            property['super_area'] = super_area
            property['furnishing'] = furnishing
        property['car_parking'] = car_parking
        property['status'] = status
        property['date_posted'] = ' '.join([str(elem) for elem in date_posted])

        # yield {
        #     'property': property
        # }
        #
        item = property

        yield item
