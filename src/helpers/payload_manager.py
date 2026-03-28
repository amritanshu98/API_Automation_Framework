#contains JSON Data

def payload_create_booking():
    payload = {
        "firstname": "Amrit",
        "lastname": "Kumar",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-03",
            "checkout": "2026-02-05"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload

def payload_update_booking():
    payload = {
        "firstname": "Lucky",
        "lastname": "Sharma",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-03-11",
            "checkout": "2026-04-15"
        },
        "additionalneeds": "Breakfast, Lunch, WiFi"
    }
    return payload