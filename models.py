from typing import List, Optional, Tuple

from pydantic import BaseModel


class Poi(BaseModel):
    name: str
    description: Optional[str] = None
    address: Optional[str] = None
    category: str
    latitude: float
    longitude: float
    open_hour: int
    close_hour: int
    picture_url: str


class ListOfPois(BaseModel):
    list_of_poi: List[Poi]


class TimedPoi(BaseModel):
    poi: Poi
    time_spent: float


class ListOfTimedPois(BaseModel):
    list_of_poi: List[TimedPoi]


class GeoPoint(BaseModel):
    lat: float
    lng: float


class Polygon(BaseModel):
    list_of_points: List[GeoPoint]


class Trip(BaseModel):
    list_of_poi: ListOfTimedPois
    transit_times: List[float]
    starting_time: List[float]
    route: List[GeoPoint]
    bounds: Tuple[Tuple[float, float], Tuple[float, float]]


class RecommendedTrips(BaseModel):
    trips: List[Trip]


class PlanTripRequest(BaseModel):
    chosen_pois: ListOfTimedPois
    start_time: str
    end_time: str
    number_of_trips: int
    city: str

class PointRequest(BaseModel):
    latlng: GeoPoint
    city: str

class PolygoinRequest(BaseModel):
    point: Polygon
    city: str
