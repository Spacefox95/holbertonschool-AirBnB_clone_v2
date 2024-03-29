#!/usr/bin/python3
"""Place Module for HBNB project"""
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
import models

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    """ For DBStorage"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False,
                                 back_populates='place_amenities')
    else:
        """ For FileStorage"""
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """
            Returns list of Review instances with place_id == current Place.if
            """
            review_list = []
            for reveiw in models.storage.all("Review").values():
                if reveiw.place_id == self.id:
                    review_list.append(reveiw)
            return review_list

        @property
        def amenities(self):
            """Getter property for amenities"""
            return self.amenities

        @amenities.setter
        def amenities(self, value):
            """Setter property for amenities"""
            from models import storage
            amenities_list = []
            for value in storage.all(Amenity).values():
                if value in self.amenity_ids:
                    amenities_list.append(value)
            self.amenity_ids = amenities_list
