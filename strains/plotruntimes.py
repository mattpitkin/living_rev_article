#!/usr/bin/env python

"""
Script to generate a plot of observing run times of various interferometric gravitational wave detectors
for the initial detector era (TAMA300, GEO600, LIGO and Virgo).

Copyright: Matthew Pitkin, 2016
"""

from __future__ import division

from collections import OrderedDict as orddic

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as pl

mplparams = {
      'backend': 'Agg',
      'text.usetex': True, # use LaTeX for all text
      'axes.linewidth': 0.5, # set axes linewidths to 0.5
      'axes.grid': True, # add a grid
      'grid.linewidth': 0.5,
      'grid.alpha': 0.3,
      'font.family': 'sans-serif',
      'font.sans-serif': 'Avant Garde, Helvetica, Computer Modern Sans serif',
      'font.size': 18 }

mpl.rcParams.update(mplparams)

# offsets for text run label placement
runyoffsetbelow = -0.4
runyoffsetabove = 0.2

# set LIGO run times [start end] (years)
LIGO = {'S1': {'times': [(2002+(7/12)+(23/365.25)), (2002+(8/12)+(9/365.25))],  'textoffset': runyoffsetbelow, 'kwargs': {'marker': 'o'}},
        'S2': {'times': [(2003+(1/12)+(14/365.25)), (2003+(3/12)+(14/365.25))], 'textoffset': runyoffsetbelow, 'kwargs': {'marker': 'o'}},
        'S3': {'times': [(2003+(9/12)+(31/365.25)), (2004+(9/365.25))],         'textoffset': runyoffsetbelow, 'kwargs': {'marker': 'o'}},
        'S4': {'times': [(2005+(1/12)+(22/365.25)), (2005+(2/12)+(23/365.25))], 'textoffset': runyoffsetbelow, 'kwargs': {'marker': 'o'}},
        'S5': {'times': [(2005+(10/12)+(4/365.25)), (2007+(9/12))],             'textoffset': runyoffsetbelow, 'kwargs': {'marker': 'o'}},
        'Astrowatch': {'times': [(2008 + (1/12) + (7/365.25)), (2009 + (4/12) + (28/365.25))], 'textoffset': runyoffsetbelow, 'kwargs': {'marker': None, 'alpha': 0.45}},
        'S6': {'times': [(2009+(6/12)+(7/365.25)), (2010+(9/12)+(20/365.25))],  'textoffset': runyoffsetbelow, 'kwargs': {'marker': 'o'}}}

# GEO600 science runs (S1-6)
GEO = {'S1':   {'times': LIGO['S1']['times'], 'textoffset': runyoffsetbelow, 'kwargs': {'marker': 'o'}},
       'S3I':  {'times': [(2003+(10/12)+(5/365.25)), (2003+(10/12)+(11/365.25))], 'textoffset': runyoffsetabove, 'kwargs': {'marker': 'o'}},
       'S3II': {'times': [(2003+(11/12)+(30/365.25)), (2004+(13/365.25))], 'textoffset': runyoffsetbelow, 'kwargs': {'marker': 'o'}},
       'S4':   {'times': LIGO['S4']['times'], 'textoffset': runyoffsetbelow, 'kwargs': {'marker': 'o'}},
       'preS5':{'times': [(2006+20/365.25), (2006+(4/12))], 'textoffset': runyoffsetbelow*1e6, 'kwargs': {'marker': 'o', 'alpha': 0.45}}, # pre-S5 overnight and weekend astrowatch
       'S5':   {'times': [(2006+(4/12)), (2006+(9/12)+(15/365.25))], 'textoffset': runyoffsetbelow, 'kwargs': {'marker': 'o'}},
       'Astrowatch': {'times': [(2006+(9/12)+(15/365.25)), (2009+(6/12)+(7/365.25))], 'textoffset': runyoffsetbelow, 'kwargs': {'marker': 'o', 'alpha': 0.45}}, # to start of S6
       'S6/Astrowatch': {'times': [(2009 + (6/12) + (7/365.25)), 2012], 'textoffset': runyoffsetbelow, 'kwargs': {'marker': '>', 'alpha': 0.45}}}

# TAMA data taking runs (DT1-9)
TAMA = {'DT1': {'times': [(1999+(7/12)+(6/365.25)),   (1999+(7/12)+(7/365.25))],  'textoffset': runyoffsetbelow, 'kwargs': {'marker': 'o'}},
        'DT2': {'times': [(1999+(8/12)+(17/365.25)),  (1999+(8/12)+(20/365.25))], 'textoffset': runyoffsetabove, 'kwargs': {'marker': 'o'}},
        'DT3': {'times': [(2000+(3/12)+(20/365.25)),  (2000+(3/12)+(23/365.25))], 'textoffset': runyoffsetbelow, 'kwargs': {'marker': 'o'}},
        'DT4': {'times': [(2000+(7/12)+(21/365.25)),  (2000+(8/12)+(4/365.25))],  'textoffset': runyoffsetbelow, 'kwargs': {'marker': 'o'}},
        'DT5': {'times': [(2001+(2/12)+(2/365.25)),   (2001+(2/12)+(8/365.25))],  'textoffset': runyoffsetbelow, 'kwargs': {'marker': 'o'}},
        'DT6': {'times': [(2001+(7/12)+(0/365.25)),   (2001+(8/12)+(20/365.25))], 'textoffset': runyoffsetbelow, 'kwargs': {'marker': 'o'}},
        'DT7': {'times': [(2002+(7/12)+(31/365.25)),  (2002+(8/12)+(2/365.25))],  'textoffset': runyoffsetbelow, 'kwargs': {'marker': 'o'}},
        'DT8': {'times': LIGO['S2']['times'], 'textoffset': runyoffsetbelow, 'kwargs': {'marker': 'o'}},
        'DT9': {'times': [(2003+(10/12)+(28/365.25)), (2004+10/365.25)], 'textoffset': runyoffsetbelow, 'kwargs': {'marker': 'o'}}}

# Virgo runs, weekend science run (WSR) and VSR1-4
VIRGO = {'WSR1': {'times': [(2006+(8/12)+(8/365.25)), (2007+(2/12)+(12/365.25))], 'textoffset': runyoffsetbelow*1e6, 'kwargs': {'marker': 'o', 'alpha': 0.45}},
         'VSR1': {'times': [(2007+(4/12)+(18/365.25)), (2007+(9/12))], 'textoffset': runyoffsetbelow, 'kwargs': {'marker': 'o'}},
         'A5':   {'times': [(2007+(9/12)), (2009+(6/12)+(7/365.25))], 'textoffset': runyoffsetbelow*1e6, 'kwargs': {'marker': 'o', 'alpha': 0.45}},
         'VSR2': {'times': [(2009+(6/12)+(7/365.25)), (2010+(8/365.25))], 'textoffset': runyoffsetbelow, 'kwargs': {'marker': 'o'}},
         'VSR3': {'times': [(2010+(7/12)+(11/365.25)), (2010+(6/12)+(20/365.25))], 'textoffset': runyoffsetbelow, 'kwargs': {'marker': 'o'}},
         'VSR4': {'times': [(2011+(5/12)+(3/365.25)), (2011+(8/12)+(5/365.25))], 'textoffset': runyoffsetbelow, 'kwargs': {'marker': 'o'}}}

# create figure
fig = pl.figure(figsize=(18, 5))

# get axes
ax = pl.gca()

# draw some thin horozinatal lines for asthetics
ax.plot([1999, 2012], [1, 1], 'k--', linewidth=0.5)
ax.plot([1999, 2012], [2, 2], 'k--', linewidth=0.5)
ax.plot([1999, 2012], [3, 3], 'k--', linewidth=0.5)
ax.plot([1999, 2012], [4, 4], 'k--', linewidth=0.5)

# detector positions in plot
detpos = orddic([('LIGO', 1), ('GEO600', 2), ('TAMA300',  3), ('Virgo', 4)])

# plot LIGO runs
for run in LIGO:
  LIGO[run]['kwargs']['color'] = 'm'
  LIGO[run]['kwargs']['linewidth'] = 6
  LIGO[run]['kwargs']['markersize'] = 10
  LIGO[run]['kwargs']['markeredgecolor'] = 'none'
  ax.plot(LIGO[run]['times'], [detpos['LIGO'], detpos['LIGO']], **LIGO[run]['kwargs'])
  ax.text(LIGO[run]['times'][0] + 0.5*np.diff(LIGO[run]['times']), detpos['LIGO'] + LIGO[run]['textoffset'], run, fontsize=12, ha='center')

# plot GEO600 runs
for run in GEO:
  GEO[run]['kwargs']['color'] = 'b'
  GEO[run]['kwargs']['linewidth'] = 6
  GEO[run]['kwargs']['markersize'] = 10
  GEO[run]['kwargs']['markeredgecolor'] = 'none'
  ax.plot(GEO[run]['times'], [detpos['GEO600'], detpos['GEO600']], **GEO[run]['kwargs'])
  ax.text(GEO[run]['times'][0] + 0.5*np.diff(GEO[run]['times']), detpos['GEO600'] + GEO[run]['textoffset'], run, fontsize=12, ha='center')

# plot TAMA300 runs and labels
for run in TAMA:
  TAMA[run]['kwargs']['color'] = 'r'
  TAMA[run]['kwargs']['linewidth'] = 6
  TAMA[run]['kwargs']['markersize'] = 10
  TAMA[run]['kwargs']['markeredgecolor'] = 'none'
  ax.plot(TAMA[run]['times'], [detpos['TAMA300'], detpos['TAMA300']], **TAMA[run]['kwargs'])
  ax.text(TAMA[run]['times'][0] + 0.5*np.diff(TAMA[run]['times']), detpos['TAMA300'] + TAMA[run]['textoffset'], run, fontsize=12, ha='center')

# plot Virgo runs
for run in VIRGO:
  VIRGO[run]['kwargs']['color'] = 'g'
  VIRGO[run]['kwargs']['linewidth'] = 6
  VIRGO[run]['kwargs']['markersize'] = 10
  VIRGO[run]['kwargs']['markeredgecolor'] = 'none'
  ax.plot(VIRGO[run]['times'], [detpos['Virgo'], detpos['Virgo']], **VIRGO[run]['kwargs'])
  ax.text(VIRGO[run]['times'][0] + 0.5*np.diff(VIRGO[run]['times']), detpos['Virgo'] + VIRGO[run]['textoffset'], run, fontsize=12, ha='center')

# add other LIGO annotation
ax.annotate('first lock H2', xy=(2000+(9/12)+(20/365.25), detpos['LIGO']), xytext=(2000+(9/12)+(20/365.25), detpos['LIGO']-0.5), fontsize=12,
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6, headlength=5), ha='center')
ax.annotate('full lock\\\\all detectors', xy=(2002.25, detpos['LIGO']), xytext=(2002.25, detpos['LIGO']-0.5), fontsize=12,
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6, headlength=5), ha='center', va='center')
ax.text(LIGO['S6']['times'][0] + 0.5*np.diff(LIGO['S6']['times']), detpos['LIGO'] + runyoffsetabove,
        'Enhanced LIGO', fontsize=12, ha='center')

# set plot limits
pl.xlim([1999.25, 2012])
pl.ylim([0, 5])

pl.xlabel('Year')

# set y-axis labels to detector names
ax.set_yticks([1, 2, 3, 4])
ax.set_yticklabels([detpos.keys()[detpos.values().index(v)] for v in sorted(detpos.values())])

# set x-axis ticks and labels
xticks = np.arange(1999.25, 2012.1, 0.25).tolist()
xticklabels = ['' for i in range(len(xticks))]
for i, v in enumerate(xticks):
  if v%1 == 0.:
    xticklabels[i] = str(int(v))
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels)

pl.tight_layout()

pl.show()

