# Programming in Python - An Introduction: Lab Module 05

### Description

Briefly describe the objectives of the Lab Module:

1) Practice focused unit testing with Python’s unittest, including float comparisons via assertAlmostEqual and divide-by-zero behavior.

2) Validate the data flow between modules (TimeAndDateUtil → WeatherData/LocationData/WeatherInfoContainer) and document code with docstrings.

3) Build small time/date and weather/location utilities that use sensible defaults.


### Exercise Activities

List the actions you took in implementing the Lab Module:

1) Implemented TimeAndDateUtil.getIso8601DateFromMillis() ( guarded non-negative input) and added short docstrings to the class methods.#update

2) Created the data containers: LocationData, WeatherInfoContainer (WindData, VisibilityData, CloudLayerData), and WeatherData; set default values and generated timestamp via TimeAndDateUtil.

3) 


### Unit and/or Integration Tests Executed

List the tests you exercised in validating your functionality for the Lab Module:

1) integer/float division (including divide-by-zero → 0.0); Fahrenheit↔Celsius conversions checked with assertAlmostEqual(..., places=7)

2) verified all default values; confirmed WeatherData.timestamp is within ±5 s of “now”; confirmed custom assignments persist; ensured location is not None.

3) 

EOF.
