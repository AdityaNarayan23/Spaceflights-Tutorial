from pydantic import BaseModel

class SpaceFlight(BaseModel):
    engines : float
    passenger_capacity : int
    crew : float
    d_check_complete : bool
    moon_clearance_complete : bool
    iata_approved : bool
    company_rating : float
    review_scores_rating : float  
