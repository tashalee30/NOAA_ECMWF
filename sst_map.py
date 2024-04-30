'''
Tasha Lee
PDF --> location plots sst
4/22/24
'''

import xarray as xr
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

interp_path = 'C:/Users/tasha/OneDrive/Desktop/NOAA_Saildrone/W24/interpolation_output/2019/'
interp_files = sorted(os.listdir(interp_path))

sdvars = ['BARO_PRES_MEAN','QL','QS','RH_MEAN','TEMP_AIR_MEAN',
          'TEMP_CTD_RBR_MEAN','uwnd','vwnd','wind_speed']
labels = ['sp','QL','QS','rh','Ta',
          'sst','u','v','Vwind']
names = ['Surface Pressure', 'Latent Heat Flux', 'Sensible Heat Flux', 'Relative Humidity',
         'Air Temperature', 'Sea Surface Tempurature', 'U wind', 'V wind', 'Wind Speed']
units = ["hPa","W/m\N{SUPERSCRIPT TWO}", "W/m\N{SUPERSCRIPT TWO}","%",
         "$^\circ$C","$^\circ$C","m/s","m/s","m/s"]

FIGPATH = 'C:/Users/tasha/OneDrive/Desktop/NOAA_Saildrone/BEL/'  # set figure path for save
savefig = True  # choose whether to save figure
showfig = True  # choose whether to display figure


idx = 5  # select variables; we only want to look at sst in this case

sdvar = sdvars[idx]
label = labels[idx]
name = names[idx]
unit = units[idx]

fcname = f'ecmwf_all_interpolated_{sdvar}.nc'
fc = xr.open_dataset(interp_path+fcname)
fc_sort = fc.sortby('initial')


# get all lat, lon coords of data
allLat_raw = fc_sort.observation.coords['latitude'].values[:,:,:].flatten()
allLon_raw = fc_sort.observation.coords['longitude'].values[:,:,:].flatten()

nas = np.logical_or(np.isnan(allLat_raw), np.isnan(allLon_raw))  # locate nan
allLat = allLat_raw[~nas]
allLon = allLon_raw[~nas]  # eliminate any nan values


# ensemble lower peak (1): 2.5 +- 0.5
fc1 = fc_sort.em.values[:,:,:].flatten()  # get forecast values

for i in range(0, len(fc1)):
    if 2 <= fc1[i] <= 3:
        continue  # leave values within the range
    else:
        fc1[i] = np.nan  # set all other values to nan
        
nas = np.isnan(fc1)  # locate nan
fc1_lat = allLat_raw[~nas]  # eliminate any nan values (values outside the respective range)
fc1_lon = allLon_raw[~nas]

# ensemble upper peak (2): 10 +- 0.5
fc2 = fc_sort.em.values[:,:,:].flatten()  # get forecast values

for i in range(0, len(fc2)):
    if 9.5 <= fc2[i] <= 10.5:
        continue  # leave values within the range
    else:
        fc2[i] = np.nan  # set all other values to nan
        
nas = np.isnan(fc2)  # locate nan
fc2_lat = allLat_raw[~nas]
fc2_lon = allLon_raw[~nas]

# saildrone lower peak (1): 4.5 +- 0.5
sd1 = fc_sort.observation.values[:,:,:].flatten()  # get saildrone values

for i in range(0, len(sd1)):
    if 4 <= sd1[i] <= 5:
        continue  # leave values within the range
    else:
        sd1[i] = np.nan  # set all other values to nan
        
nas = np.isnan(sd1)  # locate nan
sd1_lat = allLat_raw[~nas]
sd1_lon = allLon_raw[~nas]

# saildrone upper peak (2): 10 +- 0.5
sd2 = fc_sort.observation.values[:,:,:].flatten()  # get saildrone values

for i in range(0, len(sd2)):
    if 9.5 <= sd2[i] <= 10.5:
        continue  # leave values within the range
    else:
        sd2[i] = np.nan  # set all other values to nan
        
nas = np.isnan(sd2)  # locate nan
sd2_lat = allLat_raw[~nas]
sd2_lon = allLon_raw[~nas]


# create a map using PlateCarree projection
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 4),
                        subplot_kw={'projection': ccrs.PlateCarree()})
for i in range(0, 2):
    axs[i].add_feature(cfeature.COASTLINE, linewidth=0.8)
    axs[i].add_feature(cfeature.BORDERS, linewidth=0.5)
    axs[i].stock_img()

# plot coordinates for ensemble
ax = axs[0]

ax.scatter(allLon, allLat, color='lightgrey', s=3.2)
ax.scatter(fc1_lon, fc1_lat, color='red', s=3.2, label='2.5\u00B10.5$^\circ$C')
ax.scatter(fc2_lon, fc2_lat, color='blue', s=3.2, label='10\u00B10.5$^\circ$C')

ax.set_extent([-180, -145, 53, 77], crs=ccrs.PlateCarree())  # set figure bounds
ax.set_title('Ensemble Mean')

# plot coordinates for saildrone
ax = axs[1]

ax.scatter(allLon, allLat, color='lightgrey', s=3.2)
ax.scatter(sd1_lon, sd1_lat, color='red', s=3.2, label='4.5\u00B10.5$^\circ$C')
ax.scatter(sd2_lon, sd2_lat, color='blue', s=3.2, label='10\u00B10.5$^\circ$C')

ax.set_extent([-180, -145, 53, 77], crs=ccrs.PlateCarree())  # set figure bounds
ax.set_title('Saildrone')

# whole figure formatting
fig.suptitle(f'{name} PDF Peak Locations')  # set main figure title

fig.text(-1.35, 0.5, 'Latitude', va='bottom', ha='center',
        rotation='vertical', rotation_mode='anchor',
        transform=ax.transAxes, fontsize=13)
fig.text(-.1, -.2, 'Longitude', va='bottom', ha='center',
        rotation='horizontal', rotation_mode='anchor',
        transform=ax.transAxes, fontsize=13)  # manually set x and y labels

for i in range(0,2):
    gl = axs[i].gridlines(draw_labels=True, linewidth=0.5, linestyle='--',
             color='gray', alpha=0.5, ylocs=ax.get_yticks())  # add gridline ticks
    axs[i].legend(loc='lower right')
    gl.xlabels_top = False  # disable ticks on right and top of graph
    gl.ylabels_right = False



if showfig:
    plt.show()
if savefig:
    fig_name = f'{label}_map.svg'
    fig.savefig(FIGPATH+fig_name,dpi=80,format='svg',facecolor='w')
