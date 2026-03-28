# Contains common utilities
# read data from the Excel file
# read data from the csv,JSON file
# set the headers - application/json , application/xml


class Utils(object):

    def common_headers_json(self):
        return {"Content-Type": "application/json"}

    def common_headers_xml(self):
        return {"Content-Type": "application/xml"}

    def common_headers_put_patch_delete_basic_auth(self, basic_auth_value):
        headers = {"Content-Type": "application/json",
                "Authorization": "Basic "+ basic_auth_value}

        return headers

    def common_headers_put_patch_delete_cookie(self, token):
        headers =  {"Content-Type": "application/json",
                "Cookie": "token="+token}

        return headers

    def read_csv_file(self):
        pass

    def read_env_file(self):
        pass

    def read_database(self):
        pass
