#!/usr/bin/env python

"""
Plot Virgo sensitivity curves for the initial detector era (WSR1-10 and VSR1-4)
"""

from __future__ import division

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as pl

mplparams = {
      'backend': 'Agg',
      'text.usetex': True, # use LaTeX for all text
      'axes.linewidth': 1, # set axes linewidths to 1
      'axes.grid': True, # add a grid
      'legend.fontsize': 15,
      'grid.linewidth': 0.5,
      'grid.color': 'k',
      'grid.alpha': 0.2,
      'font.family': 'sans-serif',
      'font.sans-serif': 'Avant Garde, Helvetica, Computer Modern Sans serif',
      'font.size': 18}

mpl.rcParams.update(mplparams)

fig = pl.figure(figsize=(12,9))
ax = pl.gca()

# files containing strains
strainfiles = {'WSR1': 'S5/VIRGOWSR1.txt',
               'WSR10': 'S5/VIRGOWSR10.txt',
               'VSR1': 'S5/VIRGOVSR1.txt',
               'VSR2': 'S6/SensitivityH_VSR2_091020.txt',
               'VSR3': 'S6/Sensitivity_VSR3_20100916_5Mpc.txt',
               'VSR4': 'S6/Sensitivity_VSR4_20110805_11d8Mpc.txt',
               'SRD': 'VIRGO_DesignSensitivityH.txt'}

# colours for plotting strains (use colour blind friendly palettes e.g. http://mkweb.bcgsc.ca/biovis2012/color-blindness-palette.png)
colors = {'WSR1': (36/255, 1, 36/255), 'WSR10': (219/255, 209/255, 0), 'VSR1': (146/255, 0, 0), 'VSR2': (73/255, 0, 146/255), 'VSR3': (1, 109/255, 182/255), 'VSR4': (0, 146/255, 146/255), 'SRD': 'k'}

# legend labels for runs
labels = {'WSR1': 'Weekend Science Run 1 (8-11 Sep 2006)',
          'WSR10': 'Weekend Science Run 10 (9-12 Mar 2007)',
          'VSR1': 'VSR1 (25 May 2007)',
          'VSR2': 'VSR2 (20 Oct 2009)',
          'VSR3': 'VSR3 (16 Sep 2010)',
          'VSR4': 'VSR4 (5 Aug 2011)',
          'SRD': 'Design Goal'}

# make plot
for run in ['WSR1', 'WSR10', 'VSR1', 'VSR2', 'VSR3', 'VSR4', 'SRD']:
  strain = np.loadtxt(strainfiles[run], comments='%')
  linewidth = 1
  if run == 'SRD':
    linewidth = 3 # make SRD curve thicker
    strain = strain[:,[1,2]] # remove first column for SRD plot as it is just an index
  ax.loglog(strain[:,0], strain[:,1], color=colors[run], label=labels[run], linewidth=linewidth)

ax.set_xlim([10., 7000.])
ax.set_ylim([1e-23, 1e-16])

ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Amplitude Spectral Density (strain Hz$^{-1/2}$)')
ax.legend()

ax.set_xticks([10, 100, 1000])
ax.set_xticklabels(['$10$', '$100$', '$1000$'])
ax.grid(b=True, which='minor', color='k', alpha=0.2)

ax.legend()

fig.tight_layout()

#pl.show()
fig.savefig('../figures/VirgoSrunASDs/VirgoSrunASDs.pdf')
fig.savefig('../figures/VirgoSrunASDs/VirgoSrunASDs.eps')
fig.savefig('../figures/VirgoSrunASDs/VirgoSrunASDs.png', dpi=400)

