#!/usr/bin/env python3

from fastapi import FastAPI, HTTPException, Request, Body
from pydantic import BaseModel, validator
from typing import Optional, Dict
import xml.etree.ElementTree as ET
import uuid

app = FastAPI(title="Adaptation Layer API")

BOOKINGS: Dict[str, dict] = {}

class Booking(BaseModel):
    customer_name: str
    room_type: str
    price: float
    promo_code: Optional[str] = None

    @validator("price")
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Price must be positive")
        return v

def apply_discount(data: dict):
    if data.get("promo_code") == "DISCOUNT10":
        data["price"] = data["price"] * 0.9
    return data

def xml_to_json(xml_data: str) -> dict:
    try:
        root = ET.fromstring(xml_data)
        data = {
            "customer_name": root.find("customer_name").text,
            "room_type": root.find("room_type").text,
            "price": float(root.find("price").text),
            "promo_code": root.find("promo_code").text if root.find("promo_code") is not None else None
        }
        return data
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid XML format")

def json_to_xml(data: dict) -> str:
    root = ET.Element("booking")

    for key, value in data.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    return ET.tostring(root, encoding="unicode")

@app.post("/booking")
def create_booking(booking: Booking):
    data = booking.dict()

    # Apply business logic
    data = apply_discount(data)

    booking_id = str(uuid.uuid4())
    BOOKINGS[booking_id] = data

    return {
        "booking_id": booking_id,
        "data": data
    }

@app.post("/booking/xml")
async def create_booking_xml(xml_data: str = Body(..., media_type="application/xml")):
    json_data = xml_to_json(xml_data)

    # Validate using Pydantic
    booking = Booking(**json_data)

    data = apply_discount(booking.dict())

    booking_id = str(uuid.uuid4())
    BOOKINGS[booking_id] = data

    return {
        "booking_id": booking_id,
        "data": data
    }

@app.get("/booking/{booking_id}")
def get_booking(booking_id: str):
    if booking_id not in BOOKINGS:
        raise HTTPException(status_code=404, detail="Booking not found")

    return BOOKINGS[booking_id]

@app.get("/booking/{booking_id}/xml")
def get_booking_xml(booking_id: str):
    if booking_id not in BOOKINGS:
        raise HTTPException(status_code=404, detail="Booking not found")

    return json_to_xml(BOOKINGS[booking_id])