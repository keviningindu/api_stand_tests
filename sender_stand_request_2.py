import configuration
import requests
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH, params={"count":20})
response = get_users_table()
print(response.status_code)