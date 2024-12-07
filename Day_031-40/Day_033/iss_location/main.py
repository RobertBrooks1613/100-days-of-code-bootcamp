import requests
import json

api_request = requests.get(url="http://api.open-notify.org/iss-now.json")

try:
    api_request.raise_for_status()
except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError,
        requests.exceptions.Timeout, requests.exceptions.InvalidURL) as error:
    print(f"Error code {error}")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    iss_data = api_request.json()
    longitude = iss_data["iss_position"]["longitude"]
    latitude = iss_data["iss_position"]["latitude"]

    print(f"{latitude} , {longitude}")














    # api_request.json()
    # print(api_request.json())
    # with open("api_data.json", "w") as api_reader:
    #     write = api_request.json()
    #     api_reader.write(json.dumps(write, indent=4))
