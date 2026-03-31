# Get Response
# Create the JSON schema from "Json Schema Converter websites"
# Save that schema in name.json file


import allure
import pytest
import logging

from src.helpers.api_requests_wrapper import post_request
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import *
from src.constants.api_constants import ApiConstants
from src.utils.utils import Utils

import json
from jsonschema import validate
from jsonschema import ValidationError



class TestCreateBookingJSONSchema(object):

    def load_schema(self, filename):
        with open(filename, "r") as file:
            return json.load(file)

    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID shouldn't be null")
    @allure.description(
        "Creating a Booking from the payload and verify that booking id should not be null and status code should be 200 for the correct payload")
    def test_create_booking_json_schema(self):
        response = post_request(url=ApiConstants().url_create_booking(),
                                auth=None,
                                headers=Utils().common_headers_json(),
                                payload=payload_create_booking(),
                                in_json=False)

        verify_http_status_code(response_data=response,expected_data=200)

        file_path = "src/resources/create_booking_schema.json"
        schema = self.load_schema(file_path)

        # validate(instance=response.json(), schema=schema)

        try:
            validate(instance=response.json(), schema=schema)
        except ValidationError as e:
            print(e.message)
            pytest.fail("Schema Validation Error")
            # pytest.xfail("Schema Validation Error")