import urllib
import scrapy
from cssselect import Selector
from realestate_scrapper.items import RealestateScrapperItem


class Real_Estate(scrapy.Spider):
    name = "RES"
    start_urls = []
    city = ""
    state = ""
    property_type = ""

    def __init__(self, city=None, state=None ,property_type=None, *args, **kwargs):
        self.city = city
        self.state = state
        self.property_type = property_type
        if city is not None and property_type is not None:
            if property_type == "Residential":
                url = "https://www.magicbricks.com/property-for-sale/residential-real-estate?&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=" + city
                self.start_urls.append(url)
            elif property_type == "Commercial":
                url = "https://www.magicbricks.com/property-for-rent/commercial-real-estate?&proptype=Commercial-Office-Space,Office-ITPark-SEZ,Commercial-Shop,Commercial-Showroom&cityName=" + city
                self.start_urls.append(url)
            elif property_type == "PG":
                url = "https://www.magicbricks.com/property-for-rent/residential-paying-guest?cityName=" + city
                self.start_urls.append(url)
            elif property_type == "Plot":
                url = "https://www.magicbricks.com/property-for-sale/residential-commercial-agricultural-real-estate?&proptype=Residential-Plot,Commercial-land,Agricultural-Land&cityName=" + city + "&areaUnit=12850"
                self.start_urls.append(url)
        else:
            url = "https://www.magicbricks.com/property-for-sale/residential-real-estate?&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Ahmedabad"
            self.start_urls.append(url)
        super(Real_Estate, self).__init__(*args, **kwargs)

    def parse(self, response):
        print(f"CITY NAME : {self.city}")
        print(f"PROPERTY TYPE : {self.property_type}")
        properties = response.css('.SRCardList')
        if self.property_type != "PG":
            properties_url = properties.css('.SRCard::attr(onclick)').getall()
        else:
            properties_url = properties.css('#resultBlockWrapper::attr(onclick)').getall()
        print("TOTAL PROPERTIES IN THIS PAGE : ", end="")
        print(len(properties_url))

        for p in properties_url:
            url = p.split('\'')[1]
            property = {}
            mb_property_id = url.split('=')[1].split('?')[0]
            property['mb_property_id'] = mb_property_id
            property['property_type'] = self.property_type
            property['city'] = self.city
            property['state'] = self.state
            # yield {
            #     "url" : url,
            #     "p_id" : re_property_id.split('?')[0]
            # }
            if self.property_type == "Residential":
                yield response.follow(url, self.parse_residential_property, meta={'property': property})
            elif self.property_type == "Commercial":
                yield response.follow(url, self.parse_commercial_property, meta={'property': property})
            elif self.property_type == "PG":
                yield response.follow(url, self.parse_pg_property, meta={'property': property})
            elif self.property_type == "Plot":
                yield response.follow(url, self.parse_plot_property, meta={'property': property})

    def parse_residential_property(self, response):

        item = RealestateScrapperItem()

        property = response.meta['property']
        title = response.css('.p_bhk::text').extract()
        address = response.css('.p_address a::text').extract()
        description = response.css('#prop-detail-desc::text').extract_first()
        price = response.css('#priceSv::text').extract()
        bedrooms = response.css('.seeBedRoomDimen::text').extract_first()
        bathrooms = response.css('#firstFoldDisplay .p_infoColumn+ .p_infoColumn .p_value::text').extract_first()
        balconies = response.css('#firstFoldDisplay .p_infoColumn:nth-child(3) .p_value::text').extract_first()
        carpet_area = response.css('#coveredAreaDisplay::text').extract_first()
        super_area = response.css('#carpetAreaDisplay::text').extract_first()
        furnishing = response.css('.p_infoColumn:nth-child(4) .p_value::text').extract_first()
        car_parking = response.css('.p_infoColumn:nth-child(4) .p_value::text').extract_first()
        status = response.css('#fourthFoldDisplay .p_infoColumn:nth-child(1) .p_value::text').extract_first()
        date_posted = response.css('.postedOn::text').extract()

        user_name = response.css('.CA_agent_name::text').extract()
        registered_as = response.css('.CA_ownertype_name::text').extract_first(),
        user = {
            'name': ''.join(user_name[0].split()) if len(user_name) > 0 else None,
            'registered_as': registered_as[0] if registered_as is not None else None,
            'contact_number': "+91-xxxxxxxxxx"
        }

        property['title'] = ''.join(' '.join([str(elem) for elem in title]).split())
        property['address'] = ''.join(' '.join([str(elem) for elem in address]).split())
        property['locality'] = "Your locality name."
        property['description'] = description.strip() if description != None else None
        property['price'] = ' '.join([str(elem) for elem in price]).strip()
        property['bedrooms'] = ''.join(bedrooms.split())
        property['bathrooms'] = bathrooms
        property['balconies'] = balconies
        property['floor_number'] = 0
        property['total_floor'] = 0
        property['carpet_area'] = carpet_area
        property['super_area'] = super_area
        property['furnishing'] = furnishing
        property['car_parking'] = car_parking
        property['status'] = status
        property['date_posted'] = ' '.join([str(elem) for elem in date_posted]).strip()

        property['user'] = user

        # yield {
        #     'property': property
        # }
        #
        item['property'] = property

        yield item


    def parse_commercial_property(self, response):

        item = RealestateScrapperItem()

        property = response.meta['property']
        title = response.css('.p_bhk::text').extract()
        address = response.css('.p_address a::text').extract()
        description = response.css('#prop-detail-desc::text').extract_first()
        price = response.css('#priceSv::text').extract()
        ideal_for_business = response.css('#fourthFoldDisplay .p_infoColumn:nth-child(1) .p_value::text').extract_first()
        washrooms = response.css('.seeBedRoomDimen::text').extract_first()
        cafeteria = response.css('#firstFoldDisplay .p_infoColumn:nth-child(4) .p_value::text').extract_first()
        carpet_area = response.css('#plotAreaDisplay::text').extract_first()
        super_area = response.css('#coveredAreaDisplay::text').extract_first()
        furnishing = response.css('#firstFoldDisplay .p_infoColumn:nth-child(1) .p_value::text').extract_first()
        status = response.css('#fourthFoldDisplay .p_infoColumn:nth-child(1) .p_value::text').extract_first()
        date_posted = response.css('.postedOn::text').extract()

        user = {
            'name': ''.join(response.css('.CA_agent_name::text').extract_first().split()),
            'registered_as': response.css('.CA_ownertype_name::text').extract_first(),
            'contact_number': "+91-xxxxxxxxxx"
        }

        property['title'] = ''.join(' '.join([str(elem) for elem in title]).split())
        property['address'] = ''.join(' '.join([str(elem) for elem in address]).split())
        property['locality'] = "Your locality name."
        property['description'] = description.strip() if description != None else None
        property['price'] = ' '.join([str(elem) for elem in price]).strip()
        property['ideal_for_business'] = ''.join(' '.join([str(elem) for elem in ideal_for_business]).split()) if ideal_for_business != None else None
        property['washrooms'] = ''.join(washrooms.split()) if washrooms is not None else washrooms
        property['cafeteria'] = cafeteria
        property['floor_number'] = 0
        property['total_floor'] = 0
        property['carpet_area'] = carpet_area
        property['super_area'] = super_area
        property['furnishing'] = furnishing
        property['status'] = ''.join(' '.join([str(elem) for elem in status]).split()) if status is not None else status
        property['date_posted'] = ' '.join([str(elem) for elem in date_posted]).strip()

        property['user'] = user

        # yield {
        #     'property': property
        # }
        #
        item['property'] = property

        yield item


    def parse_pg_property(self, response):

        item = RealestateScrapperItem()

        property = response.meta['property']
        title = response.css('.pg-detail__header__info__titleblock__pgname::text').extract()
        address = response.css('._j-Load_Location_Map::text').extract()
        description = response.css('p::text').extract()
        price = response.css('.pg-detail__header__info__priceblock--price::text').extract()
        security_deposit = response.css('.pg-prop-details__info__grid--item:nth-child(1) .pg-prop-details__info__grid--value::text').extract()
        bedrooms = response.css('.pg-prop-details__info__grid--item:nth-child(11) .pg-prop-details__info__grid--value::text').extract_first()
        # bathrooms = response.css('#firstFoldDisplay .p_infoColumn+ .p_infoColumn .p_value::text').extract_first()
        # balconies = response.css('#firstFoldDisplay .p_infoColumn:nth-child(3) .p_value::text').extract_first()
        # furnishing = response.css('#firstFoldDisplay .p_infoColumn:nth-child(1) .p_value::text').extract_first()
        status = response.css('#fourthFoldDisplay .p_infoColumn:nth-child(1) .p_value::text').extract_first()
        date_posted = response.css('.postedOn::text').extract()

        user = {
            'name': ''.join(response.css('.pg-detail__header__info__actionblock__posted--name::text').extract_first().split()),
            'registered_as': "Owner",
            'contact_number': "+91-xxxxxxxxxx"
        }

        property['title'] = ''.join(' '.join([str(elem) for elem in title]).split())
        property['address'] = ''.join(' '.join([str(elem) for elem in address]).split())
        property['locality'] = "Your locality name."
        property['description'] = ' '.join(description[2].split()) if description != None else None
        property['price'] = ' '.join([str(elem) for elem in price]).strip()
        property['security_deposit'] = ' '.join([str(elem) for elem in security_deposit]).strip()
        property['bedrooms'] = ''.join(bedrooms.split())
        property['bathrooms'] = 2
        property['balconies'] = 2
        property['furnishing'] = "Semi furnished"
        property['status'] = ''.join(' '.join([str(elem) for elem in status]).split()) if status is not None else status
        property['date_posted'] = ' '.join([str(elem) for elem in date_posted]).strip()

        property['user'] = user

        # yield {
        #     'property': property
        # }
        #
        item['property'] = property

        yield item

    def parse_plot_property(self, response):

        item = RealestateScrapperItem()

        property = response.meta['property']
        title = response.css('.pg-detail__header__info__titleblock__pgname::text').extract()
        address = response.css('._j-Load_Location_Map::text').extract()
        description = response.css('.p_infoRow:nth-child(1)::text').extract()
        price = response.css('.pg-detail__header__info__priceblock--price::text').extract()
        plot_area = response.css('#plotAreaDisplay::text').extract_first()
        plot_length = response.css('#area1DimensionDisplay::text').extract_first()
        floors_allowed_for_construction = response.css('#secondFoldDisplay .p_infoColumn:nth-child(1) .p_value::text').extract_first()
        width_of_road_facing_the_plot = response.css('#secondFoldDisplay .p_infoColumn:nth-child(2) .p_value::text').extract_first()
        boundry_wall_status = response.css('#thirdFoldDisplay .p_infoColumn:nth-child(4) .p_value::text').extract_first()
        number_of_openside = response.css('#secondFoldDisplay .p_infoColumn~ .p_infoColumn+ .p_infoColumn .p_value::text').extract_first()

        status = response.css('#fourthFoldDisplay .p_infoColumn:nth-child(1) .p_value::text').extract_first()
        date_posted = response.css('.postedOn::text').extract()

        user = {
            'name': ''.join(response.css('.CA_agent_name::text').extract_first().split()) if response.css('.CA_agent_name::text').extract_first() is not None else None ,
            'registered_as': response.css('.CA_ownertype_name::text').extract_first(),
            'contact_number': "+91-xxxxxxxxxx"
        }

        property['title'] = ''.join(' '.join([str(elem) for elem in title]).split())
        property['address'] = ''.join(' '.join([str(elem) for elem in address]).split())
        property['locality'] = "Your locality name."
        property['description'] =  ''.join(' '.join([str(elem) for elem in description]).split()) if description != None else None
        property['price'] = ' '.join([str(elem) for elem in price]).strip()
        property['plot_area'] = plot_area
        property['plot_length'] = plot_length
        property['width_of_road_facing_the_plot'] = width_of_road_facing_the_plot
        property['floors_allowed_for_construction'] = floors_allowed_for_construction
        property['boundry_wall_status'] = boundry_wall_status
        property['number_of_openside'] = number_of_openside
        property['status'] = ''.join(' '.join([str(elem) for elem in status]).split()) if status is not None else status
        property['date_posted'] = ' '.join([str(elem) for elem in date_posted]).strip()

        property['user'] = user

        # yield {
        #     'property': property
        # }
        #
        item['property'] = property

        yield item

