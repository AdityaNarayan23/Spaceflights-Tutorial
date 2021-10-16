# -*- coding: utf-8 -*-
"""
Enter description here:

"""

import numpy as np
import pandas as pd
import pickle

from fastapi import FastAPI, Body, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from SpaceFlights import SpaceFlight


app = FastAPI()
templates = Jinja2Templates(directory="templates")

RFregressor_model = pickle.load(open("/Users/adityan/Work/kedro-spaceflights-tutorial/spaceflightsRepo/data/06_models/RF_regressor.pickle/2021-10-13T15.30.01.479Z/RF_regressor.pickle", "rb"))

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
    #return "Hello Everyone! Welcome to Spaceflights Price Prediction"

@app.get("/predict")
#async def predict_price(request: Request, data:SpaceFlight = Body):
async def predict_price(request: Request, engines: int, passenger_capacity : int, crew : float,
                        d_check_complete : bool, moon_clearance_complete : bool,
                        iata_approved : bool, company_rating : float,
                        review_scores_rating : float
                        ):

    print(engines,passenger_capacity,crew,d_check_complete,moon_clearance_complete,iata_approved,company_rating,review_scores_rating)
    data_array = np.array([engines,passenger_capacity,crew,d_check_complete,moon_clearance_complete,iata_approved,company_rating,review_scores_rating]).reshape(1,-1)
    prediction = RFregressor_model.predict(data_array)
    print("Predicted value :", prediction)
    prediction_text='The price of the Spaceflight is : {}'.format(prediction[0])
    print(prediction_text)
    return templates.TemplateResponse("index.html",{"request":request,"prediction_text": prediction_text})

'''
@app.post("/predict")
async def predict_price(request: Request, data:SpaceFlight):
    print("data :",data)
    engines = data.engines
    passenger_capacity = data.passenger_capacity
    crew = data.crew
    d_check_complete = data.d_check_complete
    moon_clearance_complete = data.moon_clearance_complete
    iata_approved = data.iata_approved
    company_rating = data.company_rating
    review_scores_rating = data.review_scores_rating
    data_array = np.array([engines,passenger_capacity,crew,d_check_complete,moon_clearance_complete,iata_approved,company_rating,review_scores_rating]).reshape(1,-1)
    prediction = RFregressor_model.predict(data_array)
    print("Predicted value :", prediction)
    prediction_text='The price of the Spaceflight is : {}'.format(prediction[0])
    print(prediction_text)
    return templates.TemplateResponse("index.html",{"request":request,"prediction_text": prediction_text})
'''

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

#uvicorn app:app --reload