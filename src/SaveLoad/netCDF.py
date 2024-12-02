"""
Code for managing the opening and closing of netCDF files
"""

import netCDF4 as nc
import os
from datetime import datetime

import numpy as np
import pandas as pd


def set_up_netcdf_file(out_fname, description, contact, time_range, time_step, ndim=1):
    """
    Set up the netcdf file, but don't write any data to it.
    :param out_fname: str, output file name
    :param description: str, description of the file
    :param contact: str, contact details of creator
    :param time_range: [start_date, end_date] with dates in format 'yyyy/mm/dd'
    :param time_step: int, time step in seconds
    :param ndim: int, number of points in the x, y, z dimensions
    :return: netcdf file object
    """

    # create file and write global attributes
    file = nc.Dataset(out_fname, 'w', format='NETCDF4')
    file.description = description
    file.history = "Created by: %s" % (os.path.basename(__file__))
    file.creation_date = "%s" % (datetime.now())
    file.contact = contact

    # set dimensions
    start_time = datetime.strptime(time_range[0], "%Y/%m/%d")
    end_time = datetime.strptime(time_range[1], "%Y/%m/%d")

    # Cerate a time series variable in seconds
    file.createDimension('time', None)

    # Get the time series in seconds
    times = pd.date_range(start=start_time, end=end_time, freq='%sS' % time_step)
    times = times - times[0]
    times = times.total_seconds()

    # Create the time variable
    time = file.createVariable('time', 'f8', ('time',))
    time.units = "seconds since %s 00:00:00" % str(start_time)
    time.long_name = "time"
    time.calendar = "standard"

    # Write the time data
    time[:] = times

    # Creat the X, Y, Z dimensions
    file.createDimension('z', ndim)
    file.createDimension('y', ndim)
    file.createDimension('x', ndim)

    # Create the X, Y, Z variables
    z = file.createVariable('z', 'f8', ('z',))
    z.long_name = "z dimension"
    y = file.createVariable('y', 'f8', ('y',))
    y.long_name = "y dimension"
    x = file.createVariable('x', 'f8', ('x',))
    x.long_name = "x dimension"


    return file

def create_netcdf(lat, lon, df, out_fname, description):
    """
    Create a netcdf file to run LSM with. This won't work in reality until we
    gap fill...
    """
    # ndim = 1
    # n_timesteps = len(df)
    # times = []
    # secs = 0.0
    # for i in range(n_timesteps):
    #    times.append(secs)
    #    print(times)
    #    secs += 1800.

    # Bit of a faff here, but we have gaps in the timeseries so we need to
    # account for them in the date index. We really need to gapfill...
    start_date = df.index[0]
    end_date = df.index[-1]

    times = []
    for i in range(len(df)):
        secs = (df.index[i] - start_date).total_seconds()
        times.append(secs)

    ndim = 1
    n_timesteps = len(df)

    # create file and write global attributes
    f = nc.Dataset(out_fname, 'w', format='NETCDF4')
    f.description = description
    f.history = "Created by: %s" % (os.path.basename(__file__))
    f.creation_date = "%s" % (datetime.now())
    f.contact = "mdekauwe@gmail.com"

    # set dimensions
    f.createDimension('time', None)
    f.createDimension('z', ndim)
    f.createDimension('y', ndim)
    f.createDimension('x', ndim)
    # f.Conventions = "CF-1.0"

    # create variables
    time = f.createVariable('time', 'f8', ('time',))
    time.units = "seconds since %s 00:00:00" % (df.index[0])
    time.long_name = "time"
    time.calendar = "standard"

    z = f.createVariable('z', 'f8', ('z',))
    z.long_name = "z"
    z.long_name = "z dimension"

    y = f.createVariable('y', 'f8', ('y',))
    y.long_name = "y"
    y.long_name = "y dimension"

    x = f.createVariable('x', 'f8', ('x',))
    x.long_name = "x"
    x.long_name = "x dimension"

    latitude = f.createVariable('latitude', 'f8', ('y', 'x',))
    latitude.units = "degrees_north"
    latitude.missing_value = -9999.
    latitude.long_name = "Latitude"

    longitude = f.createVariable('longitude', 'f8', ('y', 'x',))
    longitude.units = "degrees_east"
    longitude.missing_value = -9999.
    longitude.long_name = "Longitude"

    SWdown = f.createVariable('SWdown', 'f8', ('time', 'y', 'x',))
    SWdown.units = "W/m^2"
    SWdown.missing_value = -9999.
    SWdown.long_name = "Surface incident shortwave radiation"
    SWdown.CF_name = "surface_downwelling_shortwave_flux_in_air"

    # CABLE
    # Tair = f.createVariable('Tair', 'f8', ('time', 'z', 'y', 'x',))
    # JULES
    Tair = f.createVariable('Tair', 'f8', ('time', 'y', 'x',))
    Tair.units = "K"
    Tair.missing_value = -9999.
    Tair.long_name = "Near surface air temperature"
    Tair.CF_name = "surface_temperature"

    # Rainf = f.createVariable('Rainf', 'f8', ('time', 'y', 'x',))
    # Rainf.units = "mm/s"
    # Rainf.missing_value = -9999.
    # Rainf.long_name = "Rainfall rate"
    # Rainf.CF_name = "precipitation_flux"

    Precip = f.createVariable('Precip', 'f8', ('time', 'y', 'x',))
    Precip.units = "mm/s"
    Precip.missing_value = -9999.
    Precip.long_name = "Rainfall rate"
    Precip.CF_name = "precipitation_flux"

    Qair = f.createVariable('Qair', 'f8', ('time', 'y', 'x',))
    Qair.units = "kg/kg"
    Qair.missing_value = -9999.
    Qair.long_name = "Near surface specific humidity"
    Qair.CF_name = "surface_specific_humidity"

    # Wind = f.createVariable('Wind', 'f8', ('time', 'z', 'y', 'x',))
    Wind = f.createVariable('Wind', 'f8', ('time', 'y', 'x',))
    Wind.units = "m/s"
    Wind.missing_value = -9999.
    Wind.long_name = "Scalar windspeed";
    Wind.CF_name = "wind_speed"

    Psurf = f.createVariable('Psurf', 'f8', ('time', 'y', 'x',))
    Psurf.units = "Pa"
    Psurf.missing_value = -9999.
    Psurf.long_name = "Surface air pressure"
    Psurf.CF_name = "surface_air_pressure"

    LWdown = f.createVariable('LWdown', 'f8', ('time', 'y', 'x',))
    LWdown.units = "W/m^2"
    LWdown.missing_value = -9999.
    LWdown.long_name = "Surface incident longwave radiation"
    LWdown.CF_name = "surface_downwelling_longwave_flux_in_air"

    CO2air = f.createVariable('CO2air', 'f8', ('time', 'z', 'y', 'x',))
    CO2air.units = "ppm"
    CO2air.missing_value = -9999.
    CO2air.long_name = ""
    CO2air.CF_name = ""

    za_tq = f.createVariable('za_tq', 'f8', ('y', 'x',))
    za_tq.units = "m"
    za_tq.missing_value = -9999.
    za_tq.long_name = "level of lowest atmospheric model layer"

    za_uv = f.createVariable('za_uv', 'f8', ('y', 'x',))
    za_uv.units = "m"
    za_uv.missing_value = -9999.
    za_uv.long_name = "level of lowest atmospheric model layer"

    # write data to file
    x[:] = ndim
    y[:] = ndim
    z[:] = ndim
    time[:] = times
    latitude[:] = lat
    longitude[:] = lon

    SWdown[:, 0, 0] = df.Swdown.values.reshape(n_timesteps, ndim, ndim)
    # Rainf[:,0,0] = df.Rainf.values.reshape(n_timesteps, ndim, ndim)
    Precip[:, 0, 0] = df.Rainf.values.reshape(n_timesteps, ndim, ndim)
    Qair[:, 0, 0] = df.Qair.values.reshape(n_timesteps, ndim, ndim)
    # CABLE
    # Tair[:,0,0,0] = df.Tair.values.reshape(n_timesteps, ndim, ndim, ndim)
    # JULES
    Tair[:, 0, 0] = df.Tair.values.reshape(n_timesteps, ndim, ndim)
    # Wind[:,0,0,0] = df.Wind.values.reshape(n_timesteps, ndim, ndim, ndim)
    Wind[:, 0, 0] = df.Wind.values.reshape(n_timesteps, ndim, ndim)
    Psurf[:, 0, 0] = df.Psurf.values.reshape(n_timesteps, ndim, ndim)
    LWdown[:, 0, 0] = df.LWdown.values.reshape(n_timesteps, ndim, ndim)
    CO2air[:, 0, 0, 0] = df.CO2air.values.reshape(n_timesteps, ndim, ndim, ndim)

    # Height from Wilkinson, M., Eaton, E. L., Broadmeadow, M. S. J., and
    # Morison, J. I. L.: Inter-annual variation of carbon uptake by a
    # plantation oak woodland in south-eastern England, Biogeosciences, 9,
    # 5373–5389, https://doi.org/10.5194/bg-9-5373-2012, 2012.
    za_tq[:] = 28.  # temp - don't know measurement height
    za_uv[:] = 28.  # wind - don't know measurement height

    f.close()