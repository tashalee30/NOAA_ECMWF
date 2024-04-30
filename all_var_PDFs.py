'''
Tasha Lee
All variable PDF
4/12/24
'''

import xarray as xr
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

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

FIGPATH = 'C:/Users/tasha/OneDrive/Desktop/NOAA_Saildrone/S24/manuscript/3-results/'
savefig = False  # choose whether to save figure
showfig = True  # choose whether to display figure

# create figure
fig, axs = plt.subplots(nrows=3, ncols=1, figsize=(6, 15), layout="constrained")


idxs = [1, 2, 4, 5]  # select variables

for i in range(0, len(idxs)):  # loop through the selected variables
    idx = idxs[i]
    sdvar = sdvars[idx]
    label = labels[idx]
    name = names[idx]
    unit = units[idx]
    # ax = axes[idx]

    fcname = f'ecmwf_all_interpolated_{sdvar}.nc'
    fc = xr.open_dataset(interp_path+fcname)
    fc_sort = fc.sortby('initial')
    # print(fc_sort)

    leadtimes = [1, 21, 41, 61]  # marker for 6 hour, 5 day, 10 day, 15 day lead times
    subtitles = ['6 hour to 5 day lead time',
                 '5 to 10 day lead time',
                 '10 to 15 day lead time']  # set subtitles for each subplot
    
    for j in range(0, 3):
        a = leadtimes[j]
        b = leadtimes[j+1]  # set lead time interval (1:21, 21:41, 41:61)
        
        ax = axs[j]  # select axes
        subtitle = subtitles[j]  # select subtitle
        
        fcData = fc_sort.prediction[:,:,a:b,:].values.flatten()  # F(i,k,t,n)
        sdData = fc_sort.observation[:,:,a:b].values.flatten()  # F(i,k,t)
        emData = fc_sort.em[:,:,a:b].values.flatten()  # F(i,k,t)

        sns.kdeplot(ax=ax,x=fcData,label='Ensemble Members',fill=True,color='silver',
                    alpha=0.5)  # plot fcData
        sns.kdeplot(ax=ax,x=emData,label='Ensemble Mean',fill=True,
                    color='steelblue',alpha=0.5)
        sns.kdeplot(ax=ax,x=sdData,label='Saildrone',fill=True,
                    color='#F67E4B',alpha=0.5)

        ax.set_title(subtitle)
        ax.set_xlabel(unit)

    # set whole figure labels
    fig.suptitle(f'{name} PDF')
    axs[0].legend(loc='upper right')

    if showfig:
        plt.show()
    if savefig:
        fig_name = f'{label}_pdf.svg'
        fig.savefig(figpath+fig_name,dpi=80,format='svg',facecolor='w')


