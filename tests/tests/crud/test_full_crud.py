# Create Booking ID
# Get Booking ID
# Update the Booking(Put) - BookingID, Token
# Delete the Booking

import allure

from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import  *
from src.helpers.payload_manager import *
from src.constants.api_constants import ApiConstants
from src.utils.utils import Utils

class TestCrudBooking(object):
    @allure.title("Test CRUD Operation Create")
    @allure.description("Verify Create Booking with the with full payload is working")
    def test_create_booking_id_token(self):
        post_url = ApiConstants().url_create_booking()
        response = post_request(
            url=post_url,
            auth=None,
            headers=Utils().common_headers_json(),
            payload=payload_update_booking(),
            in_json=False
        )

        # print(response.json())
        verify_http_status_code(response_data=response, expected_data=200)
        verify_json_key_for_not_null(response.json()["bookingid"])


    @allure.title("Test CRUD Operation Get")
    @allure.description("Verify that Get Booking with the Booking ID and Token is working")
    def test_get_booking_id(self, get_booking_id):
        booking_id = get_booking_id
        get_url = ApiConstants.url_get(booking_id=booking_id)
        response = get_request_booking_id(
            url=get_url,
            auth=None,
            headers=Utils().common_headers_json(),
            in_json=False
        )
        # print(response.json())
        verify_http_status_code(response_data=response, expected_data=200)

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

        # print(response.json())
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
        # print(response.text)
        verify_http_status_code(response_data=response, expected_data=201)
        verify_response_delete(response=response.text)