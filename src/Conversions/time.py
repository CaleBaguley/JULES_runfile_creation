"""
A set of functions to convert between different time formats
"""

# ---- Constants ----
# Seconds per unit time
SECONDS_PER_HALF_HOUR: float = 1800.
SECONDS_PER_HOUR: float = 3600.
SECONDS_PER_DAY: float = 86400.


# ---- Conversion functions ----
# -- seconds and half an hour --
def half_hours_to_seconds(time_in_half_hours):
    """
    Convert from half hour units to seconds
    @param time_in_half_hours:
    @return: time in seconds
    """
    return time_in_half_hours * SECONDS_PER_HALF_HOUR


def seconds_to_half_hours(time_in_seconds):
    """
    Convert from seconds to half hour units
    @param time_in_seconds:
    @return:
    """
    return time_in_seconds / SECONDS_PER_HALF_HOUR


# -- seconds and hours --
def hours_to_seconds(time_in_hours):
    """
    Convert from hours to seconds
    @param time_in_hours:
    @return: time in seconds
    """
    return time_in_hours * SECONDS_PER_HOUR


def seconds_to_hours(time_in_seconds):
    """
    Convert from seconds to hours
    @param time_in_seconds:
    @return: time in hours
    """
    return time_in_seconds / SECONDS_PER_HOUR


# -- seconds and days --
def days_to_seconds(time_days):
    """
    Convert time from days to seconds
    @param time_days:
    @return: time in seconds
    """
    return time_days * SECONDS_PER_DAY


def seconds_to_days(time_seconds):
    """
    Convert time from seconds to days
    @param time_seconds:
    @return: time in days
    """
    return time_seconds / SECONDS_PER_DAY

