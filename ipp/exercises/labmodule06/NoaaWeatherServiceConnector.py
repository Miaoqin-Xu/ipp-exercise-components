import json
import requests

from ipp.exercises.labmodule05.LocationData import LocationData
from ipp.exercises.labmodule06.NoaaWeatherDataParser import NoaaWeatherDataParser
from ipp.exercises.labmodule06.WeatherServiceConnector import WeatherServiceConnector


class NoaaWeatherServiceConnector(WeatherServiceConnector):
    def __init__(self):
        # Initialize the base class, but inject a NoaaWeatherDataParser
        super().__init__(dataParser=NoaaWeatherDataParser())

    def _createRequestUrl(
        self,
        stationID: str = None,
        locData: LocationData = None
    ):
        """
        Build the NOAA API URL for the latest observations.
        Expected format:
        https://api.weather.gov/stations/{stationID}/observations/latest
        """

        # Build and return the URL using baseUrl from the config
        # NOTE: f"{self.baseUrl}/stations/{stationID}/observations/latest"
        return f"{self.baseUrl}/stations/{stationID}/observations/latest"

    def _getLatestWeatherData(
        self,
        requestUrl: str = None,
        stationID: str = None,
        locData: LocationData = None
    ) -> dict:
        """
        Use the existing requests.Session() (self.clientSession) to GET
        the latest weather data from NOAA. Return a cleaned-up dict
        representing the response, or None if something goes wrong.
        """

        try:
            print(f"Requesting current weather observations: {requestUrl}")

            weatherResponse = self.clientSession.get(
                requestUrl,
                timeout=self.requestTimeout
            )

            # Check status code
            if weatherResponse.status_code != 200:
                print(
                    f"Failed to get weather data. "
                    f"Response code: HTTP {weatherResponse.status_code}"
                )
                return None

            # Convert to Python dict
            responseData = weatherResponse.json()

            # Add location info into the response if it's not already present.
            # (NOAA data may not include this, so we enrich it from locData.)
            if 'location' not in responseData and locData:
                responseData['location'] = {
                    'city': locData.city,
                    'state': locData.region,
                    'country': locData.country
                }

            # Add geometry (lat/long) to match what the parser expects.
            if 'geometry' not in responseData and locData:
                responseData['geometry'] = {
                    'coordinates': [locData.longitude, locData.latitude]
                }

            # Clean up JSON-LD metadata we don't actually need for parsing
            latestRawData = responseData.copy()
            latestRawData.pop('@context', None)

            print("Successfully retrieved raw weather data")

            return latestRawData

        except requests.exceptions.Timeout:
            print("Request timed out")
            return None

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

        except (KeyError, IndexError) as e:
            print(f"Unexpected response format: {e}")
            return None
