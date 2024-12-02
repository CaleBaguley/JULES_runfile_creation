"""
A set of functions for converting between various units associated with light.
"""

import numpy as np

# -- Conversion constants: --
# radiation conversions
PHOTOSYNTHETICALLY_ACTIVE_RADIATION_PER_UNIT_SHORT_WAVE_RADIATION: float = 0.5
JOULES_PER_MICRO_MOLE_OF_LIGHT: float = 1/4.57  # J umol-1


# ---- Conversion functions: ----
# -- Photosynthetically active radiation and short wave conversions --
def short_wave_to_photosynthetically_active_radiation(short_wave_radiation):
    """
    convert short wave radiation to photosynthetically active radiation
    @param short_wave_radiation:
    @return: photosynthetically active radiation
    """
    return short_wave_radiation * PHOTOSYNTHETICALLY_ACTIVE_RADIATION_PER_UNIT_SHORT_WAVE_RADIATION


def photosynthetically_active_radiation_to_short_wave(photosynthetically_active_radiation):
    """
    convert short wave radiation to photosynthetically active radiation
    @param photosynthetically_active_radiation:
    @return: short wave radiation
    """
    return photosynthetically_active_radiation / PHOTOSYNTHETICALLY_ACTIVE_RADIATION_PER_UNIT_SHORT_WAVE_RADIATION


# -- micromoles of light and joules --
def micro_moles_of_light_to_joules(micro_moles_of_light):
    """
    Converts from photons of light in micromoles to energy in joules
    @param micro_moles_of_light: photons of light in micromoles
    @return: energy in joules
    """
    return micro_moles_of_light * JOULES_PER_MICRO_MOLE_OF_LIGHT


def light_energy_in_joules_to_micro_moles_of_light(light_energy_joules):
    """
        Converts from energy in joules to photons of light in micromoles
        @param light_energy_joules: energy in photons
        @return: photons in micromoles
        """
    return light_energy_joules / JOULES_PER_MICRO_MOLE_OF_LIGHT

# -- longwave radiation --
def estimate_lwdown(tair, rh):
    """
    Synthesises downward longwave radiation based on Tair RH

    Params:
    -------
    tair : float
        air temperature [K]
    rh : float
        relative humidity [0-1]

    Reference:
    ----------
    * Abramowitz et al. (2012), Geophysical Research Letters, 39, L04808

    """
    zeroC = 273.15

    sat_vapress = 611.2 * np.exp(17.67 * ((tair - zeroC) / (tair - 29.65)))
    vapress = np.maximum(0.05, rh) * sat_vapress
    lw_down = 2.648 * tair + 0.0346 * vapress - 474.0

    return lw_down