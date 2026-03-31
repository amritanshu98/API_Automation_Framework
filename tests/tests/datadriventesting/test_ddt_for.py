# Read the CSV or Excel file
# Create a Function create_token which can take values from Excel/CSV file
# Verify the Expected_result
from http.client import responses

import openpyxl  # Read the values fron Excel/CSV files
import pytest

from src.constants.api_constants import ApiConstants
from src.helpers.api_requests_wrapper import *

from src.utils.utils import Utils


def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append(({
            "username": username,
            "password": password
        }))
    return credentials


def create_auth_request(username, password):
    payload = {'username': username, 'password': password}
    response = post_request(
        url=ApiConstants().url_create_token(),
        headers=Utils().common_headers_json(),
        auth=None,
        payload=payload,
        in_json=False
    )
    return response



def test_create_auth_with_excel():
    file_path = r"D:\Automation_via_Python\API_Automation_Framework\tests\tests\datadriventesting\data_driven_testing.xlsx"
    credentials = read_credentials_from_excel(file_path=file_path)
    print(credentials)
    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        print(username,password)
        response = create_auth_request(username=username, password=password)
        print(response)
