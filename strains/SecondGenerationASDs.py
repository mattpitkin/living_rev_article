#!/usr/bin/env python

"""
Plot 2nd generation (aLIGO, AdvVirgo, KAGRA, and O1 sensivitity curves)
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
strainfiles = {'aLIGO': 'aligo_sensitivity.txt',
               'AdvV': 'adv_sensitivity.txt',
               'O1': 'O1/H1_O1_strain.txt'}

# colours for plotting strains (use colourblind friendly palettes e.g. http://mkweb.bcgsc.ca/biovis2012/color-blindness-palette.png)
colors = {'aLIGO': (36/255, 1, 36/255), 'AdvV': (109/255, 182/255, 1), 'KAGRA': (73/255, 0, 146/255), 'O1': (219/255, 109/255, 0)}

# legend labels for runs
labels = {'aLIGO': 'aLIGO (design)',
          'AdvV': 'AdvV (design)',
          'KAGRA': 'KAGRA (design)',
          'O1': 'aLIGO H1 (O1)'}

# make plot
for run in [('aLIGO', 4), ('AdvV', 6), ('KAGRA', 1), ('O1', 1)]: # run name and index containing that data
  if run[0] != 'KAGRA':
    strain = np.loadtxt(strainfiles[run[0]])
  else:
    strain = np.zeros((2000,2))
    strain[:,0] = np.linspace(10., 4000., 2000) # frequencies
    for k, f in enumerate(strain[:,0]):
      strain[k,1] = np.sqrt(lalsimulation.SimNoisePSDKAGRA( f ))
  linewidth = 1.5
  if run == 'SRD': linewidth = 3 # make SRD curve thicker
  ax.loglog(strain[:,0], strain[:,run[1]], color=colors[run[0]], label=labels[run[0]], linewidth=linewidth)

ax.set_xlim([10., 4000.])
ax.set_ylim([1e-24, 1e-21])

ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Amplitude Spectral Density (strain Hz$^{-1/2}$)')
ax.legend()

ax.set_xticks([100, 1000])
ax.set_xticklabels(['$100$', '$1000$'])
ax.grid(b=True, which='minor', color='k', alpha=0.2)

ax.legend()

fig.tight_layout()

#pl.show()
fig.savefig('../figures/advcurves/advcurves.pdf')
fig.savefig('../figures/advcurves/advcurves.eps')
fig.savefig('../figures/advcurves/advcurves.png', dpi=400)

