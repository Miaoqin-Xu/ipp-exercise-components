import itertools

from apscheduler.schedulers.background import BackgroundScheduler

from ipp.common.ConfigUtil import ConfigUtil
from ipp.exercises.labmodule05.LocationData import LocationData
from ipp.exercises.labmodule05.WeatherData import WeatherData
from ipp.exercises.labmodule06.NoaaWeatherServiceConnector import NoaaWeatherServiceConnector
from ipp.exercises.labmodule06.WeatherDataListener import WeatherDataListener
from ipp.exercises.labmodule06.WeatherServiceConnector import WeatherServiceConnector


class WeatherServiceManager():
    def __init__(self):
        """
        Initialize the weather service manager.
        - Create a scheduler for periodic jobs.
        - Track running/connection state.
        - Prepare listener reference.
        - Load config and setup polling info.
        """
        self.scheduler = BackgroundScheduler()
        self.isRunning = False
        self.dataListener = None

        self._initProperties()

    def _initProperties(self):
        """
        Read required config values and prepare service connection state.
        - Create the weather service connector (NOAA).
        - Initialize connection/session tracking.
        - Read pollStationIDs from config and build a cycle for round-robin polling.
        """
        self.configUtil = ConfigUtil()

        # For now, always use the NOAA weather service connector
        self.weatherSvc = NoaaWeatherServiceConnector()

        self.clientSession = None
        self.isConnected = False

        self.pollStationIDs = \
            self.configUtil.getProperty(
                WeatherServiceConnector.WEATHER_SVC_SECTION_NAME,
                "pollStationIDs"
            )

        self.pollStationList = [stationID.strip() for stationID in self.pollStationIDs.split(',')]
        self.pollStationCycle = None

        if self.pollStationIDs:
            print(f"Polling weather station ID's: {self.pollStationIDs}")

            # Create an endless cycle of the station IDs so we can rotate
            self.pollStationCycle = itertools.cycle(self.pollStationList)
        else:
            # Default station fallback if config does not define any
            self.pollStationIDs = "KBOS"
            print(f"No weather station ID's defined in config file. Using default: {self.pollStationIDs}")

    def _scheduleAndStartWeatherServiceJob(self):
        """
        Configure and start the background scheduler job.
        This job will call processWeatherData() on a fixed interval.
        """
        pollRate = self.weatherSvc.getPollRate()

        self.scheduler.add_job(
            func=self.processWeatherData,
            trigger='interval',
            id=self.pollStationIDs,
            replace_existing=True,
            seconds=pollRate,
            max_instances=2,
            coalesce=True,
            misfire_grace_time=15
        )

        self.scheduler.start()

    def startManager(self):
        """
        Start the manager:
        - Connect to the weather service if not connected.
        - Start the scheduled polling job.
        - Mark running state.
        """
        success = False

        if not self.isRunning:
            print("Creating weather service client and connecting to service.")

            if not self.weatherSvc.isClientConnected():
                self.weatherSvc.connectToService()

            self._scheduleAndStartWeatherServiceJob()

            self.isRunning = True

            print("Weather station manager is now up and running!")

            success = True
        else:
            print("Client is already connected to weather service!")
            success = True

        return success

    def stopManager(self):
        """
        Stop the manager:
        - Disconnect from the weather service.
        - Shut down the scheduler.
        - Clear running state.
        """
        success = False

        if self.isRunning:
            print("Disconnecting from weather service.")

            # Disconnect from service if currently connected
            if self.weatherSvc.isClientConnected():
                self.weatherSvc.disconnectFromService()

            try:
                # Shut down the background scheduler
                self.scheduler.shutdown(wait=False)
                self.isRunning = False
                success = True
            except:
                print("Failed to shutdown scheduler. Probably not running.")
        else:
            print("No weather service connection created! Call startManager() first.")

        return success

    def _getLocationData(self, stationID: str = None):
        """
        Produce a LocationData object for a known station ID.
        Hard-coded examples for demo/testing.
        """
        if stationID == "KJFK":
            # NYC (JFK airport)
            locData = LocationData()
            locData.name = "JFK International Airport"
            locData.city = "New York"
            locData.region = "NY"
            locData.country = "USA"
            locData.latitude = 40.63972
            locData.longitude = 73.77889

            return locData

        elif stationID == "KORD":
            # ORD (O'Hare airport)
            locData = LocationData()
            locData.name = "O'Hare International Airport"
            locData.city = "Chicago"
            locData.region = "IL"
            locData.country = "USA"
            locData.latitude = 40.978611
            locData.longitude = 73.984724

            return locData

        elif stationID == "KBOS":
            # BOS (Logan airport)
            locData = LocationData()
            locData.name = "Logan International Airport"
            locData.city = "Boston"
            locData.region = "MA"
            locData.country = "USA"
            locData.latitude = 40.35843
            locData.longitude = 73.69577

            return locData

        else:
            # Unknown station -> generic fallback
            locData = LocationData()
            locData.name = stationID
            locData.city = stationID
            locData.region = stationID
            locData.country = stationID
            locData.latitude = 0.0
            locData.longitude = 0.0

            return locData

    def processWeatherData(self):
        """
        Main polling action.
        - Pick the next station ID from the cycle.
        - Build location data for that station.
        - Ask the weather service for latest data.
        - Forward the processed WeatherData to the listener (if any).
        - Return the JSON representation of the latest data.
        """

        stationID = next(self.pollStationCycle)
        print(f"Processing station ID: {stationID}")

        locData = self._getLocationData(stationID = stationID)

        rawData = self.weatherSvc.requestCurrentWeatherData(stationID = stationID, locData = locData)
        jsonData = self.weatherSvc.getLatestWeatherDataAsJson()
        wData = self.weatherSvc.getLatestWeatherData()

        # TODO: do some processing
        # For now, "processing" means: if we have a listener registered,
        # deliver the latest WeatherData object to it.
        if self.dataListener and wData:
            self.dataListener.handleIncomingWeatherData(data = wData)

        print(f"Just retrieved weather data for station ID: {stationID}\n{jsonData}\n\n")
        #print(f"Just retrieved weather data for station ID: {stationID}")

        if self.dataListener:
            self.dataListener.handleIncomingWeatherData(data = wData)

        return jsonData
    
    def setListener(self, listener: WeatherDataListener = None):
        if listener:
            self.dataListener = listener
            
    def isClientConnected(self):
        return self.isConnected

