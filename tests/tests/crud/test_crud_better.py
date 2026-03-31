# Create Token
# Create Booking ID
# Update the Booking(Put) - BookingID, Token
# Delete the Booking


# Verify that created booking id when we update we are able to update it and delete it also

import allure

from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import  *
from src.helpers.payload_manager import *
from src.constants.api_constants import ApiConstants
from src.utils.utils import Utils

class TestCrudBooking(object):
    @allure.title("Test CRUD Operation Update")
    @allure.description("Verify that full Update with the Booking ID and Token is working")
    def test_update_booking_id_token(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        put_url = ApiConstants.url_put_patch_delete(booking_id=booking_id)
        response = put_request(
            url=put_url,
            auth=None,
            headers=Utils().common_headers_put_patch_delete_cookie(token=token),
            payload=payload_update_booking(),
            in_json=False
        )

        verify_http_status_code(response_data=response, expected_data=200)
        verify_response_key(response.json()["firstname"], "Lucky")
        verify_response_key(response.json()["lastname"], "Sharma")
        verify_response_key(response.json()["additionalneeds"],"Breakfast, Lunch, WiFi")


    @allure.title("Test CRUD Operation Delete")
    @allure.description("Verify booking gets deleted with the booking ID and Token.")
    def test_delete_booking_id(self, get_booking_id,create_token):
        booking_id = get_booking_id
        token = create_token
        delete_url= ApiConstants.url_put_patch_delete(booking_id=booking_id)
        response = delete_request(
            url=delete_url,
            auth=None,
            headers=Utils().common_headers_put_patch_delete_cookie(token=token),
            in_json=False
        )

        verify_http_status_code(response_data=response, expected_data=201)
        verify_response_delete(response=response.text)



