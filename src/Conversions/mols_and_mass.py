"""
A set of functions to convert between moles and mass in grams
"""

# ---- Constants ----
# grams per unit moles
GRAMS_PER_MOLE_OF_WATER: float = 18.02
GRAMS_PER_MOLE_OF_CARBON: float = 12.


# ---- Convertion functions ----
# -- water --
def mole_water_to_gram(value_moles):
    """
    Converts from moles of water to grams
    @param value_moles: amount of water in moles
    @return: amount of water in grams
    """
    return value_moles * GRAMS_PER_MOLE_OF_WATER


def gram_water_to_mole(value_grams):
    """
    Converts from grams of water to moles
    @param value_grams: amount of water in grams
    @return: amount of water in moles
    """
    return value_grams / GRAMS_PER_MOLE_OF_WATER


# -- carbon --
def mole_carbon_to_grams(value_moles):
    """
    converts moles of carbon to grams.
    @param value_moles: moles of carbon
    @return: grams of carbon
    """
    return value_moles * GRAMS_PER_MOLE_OF_CARBON


def grams_carbon_to_moles(value_grams):
    """
    converts grams of carbon to moles.
    @param value_grams: grams of carbon
    @return: moles of carbon
    """
    return value_grams / GRAMS_PER_MOLE_OF_CARBON

