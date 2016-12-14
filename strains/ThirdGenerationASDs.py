#!/usr/bin/env python

"""
Plot 3rd generation (ET-B,C,D and Cosmic Explorer)
"""

from __future__ import division

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as pl

import lalsimulation

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
strainfiles = {'ETB': 'ET_B_data.txt',
               'ETC': 'ET_C_data.txt',
               'ETD': 'ET_D_data.txt',
               'CE': 'cosmic_explorer.txt'}

# colours for plotting strains (use colourblind friendly palettes e.g. http://mkweb.bcgsc.ca/biovis2012/color-blindness-palette.png)
colors = {'ETB': (36/255, 1, 36/255), 'ETC': (109/255, 182/255, 1), 'ETD': (73/255, 0, 146/255), 'CE': (219/255, 109/255, 0)}

# legend labels for runs
labels = {'ETB': 'ET-B',
          'ETC': 'ET-C',
          'ETD': 'ET-D',
          'CE': 'Cosmic Explorer'}

# make plot
for run in [('ETB', 1), ('ETC', 1), ('ETD', 3), ('CE', 3)]: # run name and index containing that data
  strain = np.loadtxt(strainfiles[run[0]])

  linewidth = 1.5
  if run == 'SRD': linewidth = 3 # make SRD curve thicker
  ax.loglog(strain[:,0], strain[:,run[1]], color=colors[run[0]], label=labels[run[0]], linewidth=linewidth)

ax.set_xlim([1., 4000.])
ax.set_ylim([1e-25, 1e-22])

ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Amplitude Spectral Density (strain Hz$^{-1/2}$)')
ax.legend()

ax.set_xticks([10, 100, 1000])
ax.set_xticklabels(['$10$', '$100$', '$1000$'])
ax.grid(b=True, which='minor', color='k', alpha=0.2)

ax.legend()

fig.tight_layout()

#pl.show()
fig.savefig('../figures/etcurve/etcurve.pdf')
fig.savefig('../figures/etcurve/etcurve.eps')
fig.savefig('../figures/etcurve/etcurve.png', dpi=400)

