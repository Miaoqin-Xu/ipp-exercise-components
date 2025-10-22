"""Calculations utilities.

Provides temperature conversions and a safe division helper implemented
as class methods.
"""


class CalculationsUtil:
    """Utility class exposing stateless calculations.

    Public class methods:
      - convertTempFtoC(tempInF)
      - convertTempCtoF(tempInC)
      - divideTwoNumbers(numerator, denominator)

    This class is meant to be used without instantiation.
    """

    @classmethod
    def convertTempFtoC(cls, tempInF: float) -> float:
        """Convert Fahrenheit to Celsius.

        Keyword arguments:
        tempInF -- temperature in degrees Fahrenheit (float)

        Returns:
        float -- temperature in degrees Celsius.
        """
        return (tempInF - 32.0) * 5.0 / 9.0

    @classmethod
    def convertTempCtoF(cls, tempInC: float) -> float:
        """Convert Celsius to Fahrenheit.

        Keyword arguments:
        tempInC -- temperature in degrees Celsius (float)

        Returns:
        float -- temperature in degrees Fahrenheit.
        """
        return tempInC * 9.0 / 5.0 + 32.0

    @classmethod
    def divideTwoNumbers(cls, numerator: float, denominator: float) -> float:
        """Divide two numbers with zero-division protection.

        If the denominator is zero, this method prints a notice and returns 0.0.

        Keyword arguments:
        numerator -- the numerator (float)
        denominator -- the denominator (float)

        Returns:
        float -- the quotient; 0.0 when the denominator is zero.

        Side effects:
        Prints a notice when denominator is zero.
        """
        try:
            return float(numerator / denominator)
        except ZeroDivisionError:
            print(
                f"Can't divide {numerator} by {denominator}. "
                "ZeroDivisionError thrown."
            )
            return 0.0
