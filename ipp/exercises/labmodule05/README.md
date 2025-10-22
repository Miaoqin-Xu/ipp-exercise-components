# Programming in Python - An Introduction: Lab Module 05

### Description

Briefly describe the objectives of the Lab Module:

1) Implement a utility class (CalculationsUtil) with class methods for F↔C conversion and safe division.

2) Create weather data containers (LocationData, WindData/VisibilityData/CloudLayerData, WeatherData)

3) 


### Exercise Activities

List the actions you took in implementing the Lab Module:

1) Wrote CalculationsUtil.py with convertTempFtoC, convertTempCtoF, divideTwoNumbers.

2) Implemented LocationData (dataclass), WeatherInfoContainer (wind/visibility/cloud), and WeatherData (dataclass with defaults and nested containers).

3) Added tests (test_CalculationsUtil.py, test_TimeAndDateUtil.py, test_weatherlocationdata.py) and ran with python -m unittest.


### Unit and/or Integration Tests Executed

List the tests you exercised in validating your functionality for the Lab Module:

1) Division: integers/floats, divide-by-zero returns 0.0.

2) Temperature: known F↔C pairs and C→F→C round-trip within tolerance.

3) Weather/Location: default values, field overrides, timestamp within 5s of “now”, nested containers present.

EOF.
