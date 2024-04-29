'''
Tasha Lee
3. Results
3.1 Examples from a single saildrone
Fig 3.1 - time series
'''

import xarray as xr
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib.dates import MonthLocator
import scipy.stats
from matplotlib.offsetbox import AnchoredText

interp_path = 'C:/Users/tasha/OneDrive/Desktop/NOAA_Saildrone/W24/interpolation_output/2019/'
interp_files = sorted(os.listdir(interp_path))

sdvars = ['BARO_PRES_MEAN','QL','QS','RH_MEAN','TEMP_AIR_MEAN',
          'TEMP_CTD_RBR_MEAN','uwnd','vwnd','wind_speed']
labels = ['sp','QL','QS','rh','Ta',
          'sst','u','v','Vwind']
names = ['Surface Pressure', 'Latent Heat Flux', 'Sensible Heat Flux', 'Relative Humidity',
         'Air Temperature', 'Sea Surface Tempurature', 'U wind', 'V wind', 'Wind Speed']
colors = ['#125A56', '#238F9D', '#60BCE9', '#C6DBED', '#ECEADA',
                '#F9D576', '#FD9A44', '#E94C1F', '#A01813']
units = ["hPa","W/m\N{SUPERSCRIPT TWO}", "W/m\N{SUPERSCRIPT TWO}","%",
         "$^\circ$C","$^\circ$C","m/s","m/s","m/s"]

FIGPATH = 'C:/Users/tasha/OneDrive/Desktop/NOAA_Saildrone/S24/manuscript/3-results/'
savefig = True  # decide whether you want to save figures
showfig = True

### QL, QS plot
fig, axs = plt.subplots(nrows=4, ncols=2, figsize=(9, 16), layout="constrained")

##### SELECT VARIABLE HERE
idx = 1  # 1: QL

sdvar = sdvars[idx]
label = labels[idx]
name = names[idx]
color = colors[idx]
unit = units[idx]


fcname = f'ecmwf_all_interpolated_{sdvar}.nc'
fc = xr.open_dataset(interp_path+fcname)
fc_sort = fc.sortby('initial')
# print(fc_sort)

initial = fc_sort.initial.values


# SDVAR as function of lead time; for ensemble mean, members, saildrone

### saildrone

# 1, 5, 10, 15 day leadtime
sd1 = fc_sort.observation[:,0,4].values  # sd 1033, F(i)
sd5 = fc_sort.observation[:,0,20].values
sd10 = fc_sort.observation[:,0,40].values
sd15 = fc_sort.observation[:,0,60].values

### ensemble mean
em1 = fc_sort.em[:,0,4].values
em5 = fc_sort.em[:,0,20].values
em10 = fc_sort.em[:,0,40]
em15 = fc_sort.em[:,0,60]

### ensemble members
fc1 = fc_sort.prediction[:,0,4,:]
fc5 = fc_sort.prediction[:,0,20,:]
fc10 = fc_sort.prediction[:,0,40,:]
fc15 = fc_sort.prediction[:,0,60,:]

### PLOT QL

# 1 day leadtime
ax = axs[0][0]
for i in range(0,49):
    ax.plot(initial, fc1[:,i], c='silver', alpha=0.4, lw=1)
ax.plot(initial, fc1[:,49], c='silver', lw=1, label='Ensemble Members')
ax.plot(initial, em1, c='steelblue', label='Ensemble Mean')
ax.plot(initial, sd1, c='#F67E4B', label='Saildrone')

date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_locator(MonthLocator())
ax.xaxis.set_major_formatter(date_form)

ax.legend(fontsize=7)

# 5 day
ax = axs[1][0]
for i in range(0,49):
    ax.plot(initial, fc5[:,i], c='silver', alpha=0.4, lw=1)
ax.plot(initial, fc5[:,49], c='silver', alpha=0.4, lw=1, label='Ensemble Members')
ax.plot(initial, em5, c='steelblue', label='Ensemble Mean')
ax.plot(initial, sd5, c='#F67E4B', label='Saildrone')

date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_locator(MonthLocator())
ax.xaxis.set_major_formatter(date_form)

# 10 day
ax = axs[2][0]
for i in range(0,49):
    ax.plot(initial, fc10[:,i], c='silver', alpha=0.4, lw=1)
ax.plot(initial, fc10[:,49], c='silver', alpha=0.4, lw=1, label='Ensemble Members')
ax.plot(initial, em10, c='steelblue', label='Ensemble Mean')
ax.plot(initial, sd10, c='#F67E4B', label='Saildrone')

date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_locator(MonthLocator())
ax.xaxis.set_major_formatter(date_form)

# 15 day
ax = axs[3][0]
for i in range(0,49):
    ax.plot(initial, fc15[:,i], c='silver', alpha=0.4, lw=1)
ax.plot(initial, fc15[:,49], c='silver', alpha=0.4, lw=1, label='Ensemble Members')
ax.plot(initial, em15, c='steelblue', label='Ensemble Mean')
ax.plot(initial, sd15, c='#F67E4B', label='Saildrone')

date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_locator(MonthLocator())
ax.xaxis.set_major_formatter(date_form)

### REPEAT FOR QS
##### SELECT VARIABLE HERE
idx = 2  # 2: QS

sdvar = sdvars[idx]
label = labels[idx]
name = names[idx]
color = colors[idx]
unit = units[idx]


fcname = f'ecmwf_all_interpolated_{sdvar}.nc'
fc = xr.open_dataset(interp_path+fcname)
fc_sort = fc.sortby('initial')
# print(fc_sort)

initial = fc_sort.initial.values


# SDVAR as function of lead time; for ensemble mean, members, saildrone

### saildrone

# 1, 5, 10, 15 day leadtime
sd1 = fc_sort.observation[:,0,4].values  # sd 1033, F(i)
sd5 = fc_sort.observation[:,0,20].values
sd10 = fc_sort.observation[:,0,40].values
sd15 = fc_sort.observation[:,0,60].values

### ensemble mean
em1 = fc_sort.em[:,0,4].values
em5 = fc_sort.em[:,0,20].values
em10 = fc_sort.em[:,0,40]
em15 = fc_sort.em[:,0,60]

### ensemble members
fc1 = fc_sort.prediction[:,0,4,:]
fc5 = fc_sort.prediction[:,0,20,:]
fc10 = fc_sort.prediction[:,0,40,:]
fc15 = fc_sort.prediction[:,0,60,:]

### PLOT QL

# 1 day leadtime
ax = axs[0][1]
for i in range(0,49):
    ax.plot(initial, fc1[:,i], c='silver', alpha=0.4, lw=1)
ax.plot(initial, fc1[:,49], c='silver', alpha=0.4, lw=1, label='Ensemble Members')
ax.plot(initial, em1, c='steelblue', label='Ensemble Mean')
ax.plot(initial, sd1, c='#F67E4B', label='Saildrone')

date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_locator(MonthLocator())
ax.xaxis.set_major_formatter(date_form)

# 5 day
ax = axs[1][1]
for i in range(0,49):
    ax.plot(initial, fc5[:,i], c='silver', alpha=0.4, lw=1)
ax.plot(initial, fc5[:,49], c='silver', alpha=0.4, lw=1, label='Ensemble Members')
ax.plot(initial, em5, c='steelblue', label='Ensemble Mean')
ax.plot(initial, sd5, c='#F67E4B', label='Saildrone')

date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_locator(MonthLocator())
ax.xaxis.set_major_formatter(date_form)

# 10 day
ax = axs[2][1]
for i in range(0,49):
    ax.plot(initial, fc10[:,i], c='silver', alpha=0.4, lw=1)
ax.plot(initial, fc10[:,49], c='silver', alpha=0.4, lw=1, label='Ensemble Members')
ax.plot(initial, em10, c='steelblue', label='Ensemble Mean')
ax.plot(initial, sd10, c='#F67E4B', label='Saildrone')

date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_locator(MonthLocator())
ax.xaxis.set_major_formatter(date_form)

# 15 day
ax = axs[3][1]
for i in range(0,49):
    ax.plot(initial, fc15[:,i], c='silver', alpha=0.4, lw=1)
ax.plot(initial, fc15[:,49], c='silver', alpha=0.4, lw=1, label='Ensemble Members')
ax.plot(initial, em15, c='steelblue', label='Ensemble Mean')
ax.plot(initial, sd15, c='#F67E4B', label='Saildrone')

date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_locator(MonthLocator())
ax.xaxis.set_major_formatter(date_form)




### WHOLE FIGURE FORMAT

fig.supxlabel('Dates in 2019', fontsize=13)
fig.supylabel(unit, fontsize=13)
fig.suptitle('Saildrone 1033', fontsize=15)

col_titles = ['QL','QS']
for i, ax in enumerate(axs[0,:]):
    ax.set_title(col_titles[i], fontsize=13)
    
x_ax_labs = ["1 day lead time", "5 day lead time", "10 day lead time", "15 day lead time"]
for j in range(0,2):
    for i, ax in enumerate(axs[:,j]):
        ax.set_xlabel(x_ax_labs[i], fontsize=10)



if showfig:
    plt.show()
if savefig:
    fig_name = f'3.1_1033_QL_QS.svg'
    fig.savefig(FIGPATH+fig_name,dpi=80,format='svg',facecolor='w')
    
    
