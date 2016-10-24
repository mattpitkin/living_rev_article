#!/usr/bin/env python

"""
Plot "typical" GEO sensitivity curves for the initial detector era (S1-S6)
"""

import os

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as pl

mplparams = {
      'backend': 'Agg',
      'text.usetex': True, # use LaTeX for all text
      'axes.linewidth': 1, # set axes linewidths to 1
      'axes.grid': True, # add a grid
      'legend.fontsize': 13,
      'grid.linewidth': 0.5,
      'grid.color': 'k',
      'grid.alpha': 0.2,
      'font.family': 'sans-serif',
      'font.sans-serif': 'Avant Garde, Helvetica, Computer Modern Sans serif',
      'font.size': 18}

mpl.rcParams.update(mplparams)

fig = pl.figure(figsize=(12,9))
ax = pl.gca()

# S1-S5 strain file
strains = np.loadtxt('GEOallruns.txt', comments='%')
allstrains = {'S1': strains[:,[0,1]],
              'S3I': strains[:,[0,2]],
              'S3II': strains[:,[0,3]],
              'S4': strains[:,[0,4]],
              'S5': strains[:,[0,5]],
              'S52': strains[:,[0,6]],
              'S6': np.loadtxt('S6/GEO_s6_sens.txt'),   # S6 strain file
              'S6e': np.loadtxt('S6/GEO_s6e_sens.txt'), # S6E strain file
              'SRD': np.loadtxt('GEOdesign_550HzSRC.txt', comments='%')}

# colours for plotting strains
colors = {'S1': 'g', 'S3I': 'c', 'S3II': 'aqua', 'S4': 'b', 'S5': 'm', 'S52': 'violet', 'S6': 'orangered', 'S6e': 'darksalmon', 'SRD': 'k'}

# legend labels for runs
labels = {'S1': 'S1',
          'S3I': 'S3I',
          'S3II': 'S3II',
          'S4': 'S4',
          'S5': 'S5 overnight \& weekend',
          'S52': 'S5 24/7',
          'S6': 'S6',
          'S6e': 'S6E (June-August 2011)',
          'SRD': 'theoretical design noise budget'}

# make plot
for run in ['S1', 'S3I', 'S3II', 'S4', 'S5', 'S52', 'S6', 'S6e', 'SRD']:
  strain = allstrains[run]
  linewidth = 1
  if run == 'SRD': linewidth = 3 # make SRD curve thicker
  ax.loglog(strain[:,0], strain[:,1], colors[run], label=labels[run], linewidth=linewidth)

ax.set_xlim([10., 5000.])
ax.set_ylim([5e-23, 1e-15])

ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Amplitude Spectral Density (strain Hz$^{-1/2}$)')
ax.legend()

ax.set_xticks([10, 100, 1000])
ax.set_xticklabels(['$10$', '$100$', '$1000$'])
ax.grid(b=True, which='minor', color='k', alpha=0.2)

ax.legend()

#pl.show()
fig.savefig('../figures/GEOSrunASDs/GEOSrunASDs.pdf')
fig.savefig('../figures/GEOSrunASDs/GEOSrunASDs.eps')
fig.savefig('../figures/GEOSrunASDs/GEOSrunASDs.png', dpi=400)

