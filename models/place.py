#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey, Float, String, Table
from sqlalchemy.orm import relationship
from os import getenv
from . import storage


metadata = Base.metadata
place_amenity = Table("place_amenity",
                      metadata,
                      Column("place_id", String(60), ForeignKey(
                          "places.id"), primary_key=True),
                      Column("amenity_id", String(60), ForeignKey(
                          "amenities.id"), primary_key=True)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenities = relationship(
        "Amenity", secondary="place_amenity", viewonly=False)
    reviews = relationship("Review", cascade="all, delete")
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            from .review import Review
            return [x for x in storage.all(
                Review).values() if x.place_id == self.id]

        @property
        def amenities(self):
            from .amenity import Amenity
            return [x for x in storage.all(
                Amenity).values() if x.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, value):
            from .amenity import Amenity
            if type(value) is Amenity:
                self.amenity_ids.append(value.id)
    amenity_ids = []
