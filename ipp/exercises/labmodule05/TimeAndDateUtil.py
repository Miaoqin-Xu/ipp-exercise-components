import datetime
import time

class TimeAndDateUtil():

    @classmethod
    def getCurrentLocalDateInMillis(cls):
        current_millis = time.time() * 1000

        return current_millis

    @classmethod
    def getCurrentIso8601LocalDate(cls, ignoreMillis: bool = True):
        current_date = datetime.datetime.fromtimestamp(TimeAndDateUtil.getCurrentLocalDateInMillis() / 1000)
        
        if ignoreMillis:
                current_date = current_date.replace(microsecond = 0)
        
        formatted_date = current_date.isoformat()

        return formatted_date

    @classmethod
    def getIso8601DateFromMillis(cls, millis: int = 0, ignoreMillis: bool = True):
        """Return ISO 8601 local time for a given epoch milliseconds."""
        if millis is None or millis < 0:
            raise ValueError("millis must be >= 0")

        date = datetime.datetime.fromtimestamp(millis / 1000)
        if ignoreMillis:
            date = date.replace(microsecond=0)

        formatted_date = date.isoformat()
        return formatted_date
