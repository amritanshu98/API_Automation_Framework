import allure
import pytest
import logging

from src.helpers.api_requests_wrapper import post_request
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import *
from src.constants.api_constants import ApiConstants
from src.utils.utils import Utils



class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID shouldn't be null")
    @allure.description(
        "Creating a Booking from the payload and verify that booking id should not be null and status code should be 200 for the correct payload")
    def test_create_booking_positive(self):
        response = post_request(url=ApiConstants().url_create_booking(),
                                auth=None,
                                headers=Utils().common_headers_json(),
                                payload=payload_create_booking(),
                                in_json=False)

        verify_http_status_code(response_data=response,expected_data=200)
        # booking_id = response.json()["bookingid"]
        # verify_json_key_for_not_null(booking_id)
        verify_json_key_for_not_null(response.json()["bookingid"])

    @pytest.mark.negative
    @allure.title("Verify that Create Booking with Empty payload")
    @allure.description(
        "Creating a Booking from Empty payload and verify that Status Code")
    def test_create_booking_negative(self):
        response = post_request(url=ApiConstants().url_create_booking(),
                                auth=None,
                                headers=Utils().common_headers_json(),
                                payload={},
                                in_json=False)

        verify_http_status_code(response_data=response, expected_data=500)
