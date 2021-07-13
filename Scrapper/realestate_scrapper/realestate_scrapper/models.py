from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, Text)
from scrapy.utils.project import get_project_settings

Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    Base.metadata.create_all(engine)


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True)
    name = Column('name', Text())
    registered_as = Column('registered_as', Text())
    contact_number = Column('contact_number', Text())
    residential_properties = relationship('Residential_Property', backref='user')
    commercial_properties = relationship('Commercial_Property', backref='user')
    pg_properties = relationship('PG_Property', backref='user')
    plot_properties = relationship('Plot_Property', backref='user')


class Residential_Property(Base):
    __tablename__ = "Residential_Property"

    id = Column(Integer, primary_key=True)
    mb_property_id = Column('mb_property_id', Text())
    property_type = Column('property_type', Text())
    title = Column('title', Text())
    address = Column('address', Text())
    city = Column('city', Text())
    locality = Column('locality', Text())
    state = Column('state', Text())
    description = Column('description', Text())
    price = Column('price', Text())
    bedrooms = Column('bedrooms', Text())
    bathrooms = Column('bathrooms', Text())
    balconies = Column('balconies', Text())
    floor_number = Column('floor_number', Text())
    total_floor = Column('total_floor', Text())
    carpet_area = Column('carpet_area', Text())
    super_area = Column('super_area', Text())
    furnishing = Column('furnishing', Text())
    car_parking = Column('car_parking', Text())
    status = Column('status', Text())
    date_posted = Column('date_posted', Text())
    user_id = Column(Integer, ForeignKey('User.id'))  # Many property to one user


class Commercial_Property(Base):
    __tablename__ = "Commercial_Property"

    id = Column(Integer, primary_key=True)
    mb_property_id = Column('mb_property_id', Text())
    property_type = Column('property_type', Text())
    title = Column('title', Text())
    address = Column('address', Text())
    city = Column('city', Text())
    locality = Column('locality', Text())
    state = Column('state', Text())
    description = Column('description', Text())
    price = Column('price', Text())
    ideal_for_business = Column('ideal_for_business', Text())
    cafeteria = Column('cafeteria', Text())
    washrooms = Column('washrooms', Text())
    floor_number = Column('floor_number', Text())
    total_floor = Column('total_floor', Text())
    carpet_area = Column('carpet_area', Text())
    super_area = Column('super_area', Text())
    furnishing = Column('furnishing', Text())
    status = Column('status', Text())
    date_posted = Column('date_posted', Text())
    user_id = Column(Integer, ForeignKey('User.id'))  # Many property to one user


class PG_Property(Base):
    __tablename__ = "PG_Property"

    id = Column(Integer, primary_key=True)
    mb_property_id = Column('mb_property_id', Text())
    property_type = Column('property_type', Text())
    title = Column('title', Text())
    address = Column('address', Text())
    city = Column('city', Text())
    locality = Column('locality', Text())
    state = Column('state', Text())
    description = Column('description', Text())
    price = Column('price', Text())
    security_deposit = Column('security_deposite', Text())
    bedrooms = Column('bedrooms', Text())
    bathrooms = Column('bathrooms', Text())
    balconies = Column('balconies', Text())
    furnishing = Column('furnishing', Text())
    status = Column('status', Text())
    date_posted = Column('date_posted', Text())
    user_id = Column(Integer, ForeignKey('User.id'))  # Many property to one user


class Plot_Property(Base):
    __tablename__ = "Plot_Property"

    id = Column(Integer, primary_key=True)
    mb_property_id = Column('mb_property_id', Text())
    property_type = Column('property_type', Text())
    title = Column('title', Text())
    address = Column('address', Text())
    city = Column('city', Text())
    locality = Column('locality', Text())
    state = Column('state', Text())
    description = Column('description', Text())
    price = Column('price', Text())
    floors_allowed_for_construction = Column('floors_allowed_for_construction', Text())
    number_of_openside = Column('number_of_openside', Text())
    width_of_road_facing_the_plot = Column('width_of_road_facing_the_plot', Text())
    boundry_wall_status = Column('boundry_wall_status', Text())
    plot_area = Column('plot_area', Text())
    plot_length = Column('plot_length', Text())
    status = Column('status', Text())
    date_posted = Column('date_posted', Text())
    user_id = Column(Integer, ForeignKey('User.id'))  # Many property to one user
