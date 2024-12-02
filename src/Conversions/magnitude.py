"""
A function to convert between different units of magnitude
"""

from numpy import power

# ---- Constants ----
# Dict matching si unit prefixes to their scale.
symbol_magnitude_dict = {'Y':  power(10.,  24),
                         'Z':  power(10.,  21),
                         'E':  power(10.,  18),
                         'P':  power(10.,  15),
                         'T':  power(10.,  12),
                         'G':  power(10.,   9),
                         'M':  power(10.,   6),
                         'k':  power(10.,   3),
                         'h':  power(10.,   2),
                         'da': power(10.,   1),
                         '':   power(10.,   0),
                         'd':  power(10., - 1),
                         'c':  power(10., - 2),
                         'm':  power(10., - 3),
                         'u':  power(10., - 6),
                         'n':  power(10., - 9),
                         'p':  power(10., -12),
                         'f':  power(10., -15),
                         'a':  power(10., -18),
                         'z':  power(10., -21),
                         'y':  power(10., -24)
                         }


# -- Conversion functions --
def magnitude_conversion(value, symbol_current_magnitude='', symbol_target_magnitude=''):
    """
    Function to convert between si magnitudes
    @param value: value to be converted
    @param symbol_current_magnitude: current si magnitude symbol
    @param symbol_target_magnitude: target si magnitude symbol
    @return: converted value
    """

    scale: float = symbol_magnitude_dict[symbol_current_magnitude] / symbol_magnitude_dict[symbol_target_magnitude]

    return value * scale