# Programming in Python - An Introduction: Lab Module 06

### Description

Briefly describe the objectives of the Lab Module:

1) To understand how to design and implement a modular weather data service system using Python classes and package structures.

2) To learn how to connect to an external web API (NOAA Weather Service) and request real-time weather data.

3) To integrate the different layers of the weather system, including data connectors, managers, and listeners, and verify them using unit tests.


### Exercise Activities

List the actions you took in implementing the Lab Module:

1) Implemented and verified multiple modules under `labmodule06`, including the `WeatherServiceConnector`, `NoaaWeatherServiceConnector`, and `WeatherServiceManager`.

2) Completed the main action method `processWeatherData()` by following the professor’s provided template and adding the correct “processing” logic to handle weather data and listener communication.

3) Reviewed and fixed import issues related to module paths and naming (e.g., correcting `WeatherServiceManager` filename capitalization to match Python import resolution).

4) Ran provided unit tests under `tests/labmodule06/` to validate the functionality of service connection, data request, and weather data parsing behavior.

5) Diagnosed test failures (`AssertionError: False is not true`, `AssertionError: None != 'NOAA Weather Service'`) and verified that they were caused by uninitialized configurations or missing service connections.

6) Tried to ensure successful connection to the server(Failed to fix)


### Unit and/or Integration Tests Executed

List the tests you exercised in validating your functionality for the Lab Module:

1) **`testWeatherServiceProperties`** – Verified that the weather service correctly reports its name (“NOAA Weather Service”) and other initialized properties.

2) **`testWeatherServiceRequestByStation`** – Tested that the system can successfully request current weather data for a given station ID and return a valid response.

3) **`testWeatherServiceManager`** – Confirmed that the manager correctly cycles through weather stations, retrieves data, and processes JSON output.

4) Validated the interaction between the `WeatherServiceConnector`, `NoaaWeatherServiceConnector`, and `WeatherServiceManager` through end-to-end test runs.

5) Try fixing missing import paths and re-ran all tests to confirm the system could be imported and executed cleanly without Pylance or import errors.(Don't know if helped)

EOF.
