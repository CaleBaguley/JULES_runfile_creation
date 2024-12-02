"""
A set of functions for converting between various units of temperature
"""

# -- Conversion constants: --
ZERO_DEGREES_CENTIGRADE_IN_KELVIN: float = 273.15
TWENTY_FIVE_DEGREES_CENTIGRADE_IN_KELVIN: float = 298.15


# -- Conversion functions: --
# kelvin and centigrade
def degrees_centigrade_to_kelvin(temperature_centigrade):
    """
    Convert from centigrade to kelvin
    @param temperature_centigrade:
    @return: temperature in kelvin
    """
    return temperature_centigrade + ZERO_DEGREES_CENTIGRADE_IN_KELVIN


def degrees_kelvin_to_centigrade(temperature_kelvin):
    """
    Convert from kelvin to centigrade
    @param temperature_kelvin:
    @return: temperature in centigrade
    """
    return temperature_kelvin - ZERO_DEGREES_CENTIGRADE_IN_KELVIN
