#!/usr/bin/python3
"""This is place class model"""

from models.base_model import BaseModel


class Place(BaseModel):
    """class managing place"""

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
