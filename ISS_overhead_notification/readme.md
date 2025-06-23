# Application Programming Interface (API) - ISS Overhead Notification

## What I learned
- How to interact with an API using concepts like API calls, endpoints, and parameters.
- How to handle API responses using the `requests` module.

## Code Example in Action

### `requests`

```python
import requests

MY_LAT = 37.566536
MY_LONG = 126.9779668
SUNSET_SUNRISE_URL = "https://api.sunrise-sunset.org/json"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url=SUNSET_SUNRISE_URL, params=parameters)
response.raise_for_status()

data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
```

```python
url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url=url)

# response.raise_for_status()
if response.status_code == 404:
    raise Exception("That response does not exist.")
elif response.statue_code == 401:
    raise Exception("You are not authorized to access this data")

data = response.json()
print(data)
```

- `response.status_code` indicates the HTTP response code, such as 200 (OK), 401 (Unauthorized), or 404 (Not Found).
- `response.raise_for_status()` automatically raises an exception for error codes (4xx or 5xx).
- You can also check specific status codes manually to handle different cases with custom exceptions.
