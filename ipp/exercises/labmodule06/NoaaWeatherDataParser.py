from ipp.exercises.labmodule05.LocationData import LocationData
from ipp.exercises.labmodule05.WeatherData import WeatherData
from ipp.exercises.labmodule05.WeatherInfoContainer import CloudLayerData, VisibilityData, WindData
from ipp.exercises.labmodule06.WeatherDataParser import WeatherDataParser


class NoaaWeatherDataParser(WeatherDataParser):
    def __init__(self):
        super().__init__()

    def _createWeatherDataFromRawData(
        self,
        rawData: dict,
        stationID: str,
        stationName: str
    ) -> WeatherData:
        """
        Take the NOAA API response (rawData), pull out the fields we care about,
        and build a WeatherData instance.
        """

        weather = WeatherData()
        weather.stationID = stationID
        weather.stationName = stationName

        # NOAA response seems to have 'properties' at the top level
        props = rawData.get('properties', {})
        # geometry can contain coordinates
        geometry = rawData.get('geometry', {})

        # --- Location parsing ---
        coords = geometry.get('coordinates', [])
        latitude = None
        longitude = None

        if coords and len(coords) >= 2:
            # NOAA commonly returns [longitude, latitude]
            longitude = coords[0]
            latitude = coords[1]

        loc = LocationData()
        loc.stationID = stationID
        loc.stationName = stationName
        loc.latitude = latitude
        loc.longitude = longitude

        weather.location = loc

        # --- Basic conditions ---
        # props.get('textDescription') -> e.g. "Clear", "Mostly Cloudy"
        weather.conditions = props.get('textDescription', 'N/A')

        # --- Temperature ---
        temp = props.get('temperature', {})
        # each of these NOAA fields is typically like { "unitCode": "...", "value": number }
        weather.temperature = temp.get('value') if temp.get('value') is not None else 0.0

        print(f"{weather.location.nameID} -> {weather.conditions}: {weather.temperature}")

        # --- Dewpoint ---
        dewpoint = props.get('dewpoint', {})
        weather.dewpoint = dewpoint.get('value') if dewpoint.get('value') is not None else 0.0

        # --- Wind ---
        windSpeed = props.get('windSpeed', {})
        windGust = props.get('windGust', {})
        windDirection = props.get('windDirection', {})

        wind = WindData()
        wind.windSpeed = windSpeed.get('value') if windSpeed.get('value') is not None else 0.0
        wind.windGust = windGust.get('value') if windGust.get('value') is not None else 0.0
        wind.windDirection = windDirection.get('value') if windDirection.get('value') is not None else 0.0

        weather.wind = wind

        # --- Humidity ---
        relHumidity = props.get('relativeHumidity', {})
        weather.humidity = relHumidity.get('value') if relHumidity.get('value') is not None else 0.0

        # --- Visibility ---
        vis = props.get('visibility', {})
        visibilityMeters = vis.get('value') if vis.get('value') is not None else 0.0

        visibility = VisibilityData()
        visibility.meters = visibilityMeters

        weather.visibility = visibility

        # --- Pressure ---
        pressure = props.get('barometricPressure', {})
        # NOAA gives pressure in Pascals usually.
        weather.pressure = pressure.get('value') if pressure.get('value') is not None else 0.0

        # --- Cloud layers ---
        cloudLayers = props.get('cloudLayers', [])
        weather.cloudLayers = []

        for layer in cloudLayers:
            # Each layer typically has 'base' { 'value': ... } and 'amount'
            baseData = layer.get('base', {})
            amount = layer.get('amount', '')

            cloudLayer = CloudLayerData()
            cloudLayer.baseFeet = baseData.get('value') if baseData.get('value') is not None else 0.0
            cloudLayer.amount = amount if amount is not None else ''

            print(f" -> Cloud layer {cloudLayer.amount}; base: {cloudLayer.baseFeet}")

            weather.cloudLayers.append(cloudLayer)

        return weather
