from sqlalchemy import update
from sqlalchemy.orm import sessionmaker
from realestate_scrapper.models import db_connect, create_table, User, Residential_Property, Commercial_Property, \
    PG_Property, Plot_Property


class RealestateScrapperPipeline:
    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()

        if item['property']['property_type'] == "Residential":
            property = Residential_Property()

            exist_pro = session.query(Residential_Property).filter_by(
                mb_property_id=item['property']['mb_property_id']).first()
            if exist_pro is not None:
                print("already exist")
                property = exist_pro

            print(f"PROPERTY ID : {item['property']['mb_property_id']}")

            property.mb_property_id = item['property']['mb_property_id']
            property.property_type = item['property']['property_type']
            property.title = item['property']['title']
            property.address = item['property']['address']
            property.city = item['property']['city']
            property.state = item['property']['state']
            property.locality = item['property']['locality']
            property.description = item['property']['description']
            property.price = item['property']['price']
            property.bedrooms = item['property']['bedrooms']
            property.bathrooms = item['property']['bathrooms']
            property.balconies = item['property']['balconies']
            property.floor_number = item['property']['floor_number']
            property.total_floor = item['property']['total_floor']
            property.carpet_area = item['property']['carpet_area']
            property.super_area = item['property']['super_area']
            property.furnishing = item['property']['furnishing']
            property.car_parking = item['property']['car_parking']
            property.status = item['property']['status']
            property.date_posted = item['property']['date_posted']

        elif item['property']['property_type'] == "Commercial":
            property = Commercial_Property()

            exist_pro = session.query(Commercial_Property).filter_by(
                mb_property_id=item['property']['mb_property_id']).first()
            if exist_pro is not None:
                print("already exist")
                property = exist_pro

            print(f"PROPERTY ID : {item['property']['mb_property_id']}")

            property.mb_property_id = item['property']['mb_property_id']
            property.property_type = item['property']['property_type']
            property.title = item['property']['title']
            property.address = item['property']['address']
            property.city = item['property']['city']
            property.state = item['property']['state']
            property.locality = item['property']['locality']
            property.description = item['property']['description']
            property.price = item['property']['price']
            property.ideal_for_business = item['property']['ideal_for_business']
            property.cafeteria = item['property']['cafeteria']
            property.washrooms = item['property']['washrooms']
            property.floor_number = item['property']['floor_number']
            property.total_floor = item['property']['total_floor']
            property.carpet_area = item['property']['carpet_area']
            property.super_area = item['property']['super_area']
            property.furnishing = item['property']['furnishing']
            property.status = item['property']['status']
            property.date_posted = item['property']['date_posted']


        elif item['property']['property_type'] == "PG":
            property = PG_Property()

            exist_pro = session.query(PG_Property).filter_by(
                mb_property_id=item['property']['mb_property_id']).first()
            if exist_pro is not None:
                print("already exist")
                property = exist_pro

            print(f"PROPERTY ID : {item['property']['mb_property_id']}")

            property.mb_property_id = item['property']['mb_property_id']
            property.property_type = item['property']['property_type']
            property.title = item['property']['title']
            property.address = item['property']['address']
            property.city = item['property']['city']
            property.state = item['property']['state']
            property.locality = item['property']['locality']
            property.description = item['property']['description']
            property.price = item['property']['price']
            property.security_deposit = item['property']['security_deposit']
            property.bedrooms = item['property']['bedrooms']
            property.bathrooms = item['property']['bathrooms']
            property.balconies = item['property']['balconies']
            property.furnishing = item['property']['furnishing']
            property.status = item['property']['status']
            property.date_posted = item['property']['date_posted']

        elif item['property']['property_type'] == "Plot":
            property = Plot_Property()

            exist_pro = session.query(Plot_Property).filter_by(
                mb_property_id=item['property']['mb_property_id']).first()
            if exist_pro is not None:
                print("already exist")
                property = exist_pro

            print(f"PROPERTY ID : {item['property']['mb_property_id']}")

            property.mb_property_id = item['property']['mb_property_id']
            property.property_type = item['property']['property_type']
            property.title = item['property']['title']
            property.address = item['property']['address']
            property.city = item['property']['city']
            property.state = item['property']['state']
            property.locality = item['property']['locality']
            property.description = item['property']['description']
            property.price = item['property']['price']
            property.plot_area = item['property']['plot_area']
            property.plot_length = item['property']['plot_length']
            property.floors_allowed_for_construction = item['property']['floors_allowed_for_construction']
            property.boundry_wall_status = item['property']['boundry_wall_status']
            property.number_of_openside = item['property']['number_of_openside']
            property.width_of_road_facing_the_plot = item['property']['width_of_road_facing_the_plot']
            property.date_posted = item['property']['date_posted']

        user = User()
        user.name = item['property']['user']['name']
        user.registered_as = item['property']['user']['registered_as']
        user.contact_number = item['property']['user']['contact_number']

        print(user)
        if exist_pro is None:
            property.user = user
        else:
            pass

        try:
            if exist_pro:
                session.commit()
            else:
                session.add(property)
                session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
