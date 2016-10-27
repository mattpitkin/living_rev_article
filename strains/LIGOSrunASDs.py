#!/usr/bin/env python

"""
Plot "best" LIGO sensitivity curves for the initial detector era (S1-S6)
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
strainfiles = {'S1': 'S1/llo_020907_strain.txt',
               'S2': 'S2/llo_030301_strain.txt',
               'S3': 'S3/lho4k_040104_strain.txt',
               'S4': 'S4/lho4k_050226_strain.txt',
               'S5': 'S5/lho4k_070318_strain.txt',
               'S6': 'S6/lho4k_15May2010_05hrs17min45secUTC_strain.txt',
               'SRD': 'LIGO_4k_SRD.txt'}

# colours for plotting strains (use colourblind friendly palettes e.g. http://mkweb.bcgsc.ca/biovis2012/color-blindness-palette.png)
colors = {'S1': (36/255, 1, 36/255), 'S2': (146/255, 0, 0), 'S3': (109/255, 182/255, 1), 'S4': (73/255, 0, 146/255), 'S5': (1, 109/155, 182/255), 'S6': (0, 146/255, 146/255), 'SRD': 'k'}

# legend labels for runs
labels = {'S1': 'S1 - LLO (7 Sep 2002)',
          'S2': 'S2 - LLO (1 Mar 2003)',
          'S3': 'S3 - LHO (4 Jan 2004)',
          'S4': 'S4 - LHO (26 Feb 2005)',
          'S5': 'S5 - LHO (18 Mar 2007)',
          'S6': 'S6 - LHO (15 May 2010)',
          'SRD': 'LIGO 4km design goal'}

# make plot
for run in ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'SRD']:
  strain = np.loadtxt(strainfiles[run])
  linewidth = 1
  if run == 'SRD': linewidth = 3 # make SRD curve thicker
  ax.loglog(strain[:,0], strain[:,1], color=colors[run], label=labels[run], linewidth=linewidth)

ax.set_xlim([20., 7000.])
ax.set_ylim([1e-24, 1e-16])

ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Amplitude Spectral Density (strain Hz$^{-1/2}$)')
ax.legend()

ax.set_xticks([100, 1000])
ax.set_xticklabels(['$100$', '$1000$'])
ax.grid(b=True, which='minor', color='k', alpha=0.2)

ax.legend()

fig.tight_layout()

#pl.show()
fig.savefig('../figures/LIGOSrunASDs/LIGOSrunASDs.pdf')
fig.savefig('../figures/LIGOSrunASDs/LIGOSrunASDs.eps')
fig.savefig('../figures/LIGOSrunASDs/LIGOSrunASDs.png', dpi=400)

