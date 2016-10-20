% a script to create a timeline of LIGO, GEO, VIRGO and TAMA science runs

% edit to add extra runs

% LIGO science runs (S1-6) [start end] (in years)
LIGOS1 = [(2002+(7/12)+(23/365.25)) (2002+(8/12)+(9/365.25))];
LIGOS2 = [(2003+(1/12)+(14/365.25)) (2003+(3/12)+(14/365.25))];
LIGOS3 = [(2003 + (9/12)+(31/365.25)) (2004+(9/365.25))];
LIGOS4 = [(2005 + (1/12) + (22/365.25)) (2005 + (2/12) + (23/365.25))];
LIGOS5 = [(2005 + (10/12) + (4/365.25)) (2007 + (9/12))];
LIGOA5 = [(2008 + (1/12) + (7/365.25)) (2009 + (4/12) + (28/365.25))]; % astrowatch to start of S6
LIGOS6 = [(2009 + (6/12) + (7/365.25)) (2010 + (9/12) + (20/365.25))];

% GEO600 science runs (S1-6)
GEOS1 = LIGOS1;
GEOS3I = [(2003 + (10/12) + (5/365.25)) (2003 + (10/12) + (11/365.25))];
GEOS3II = [(2003 + (11/12) + (30/365.25)) (2004 + (13/365.25))];
GEOS4 = LIGOS4;
GEOS5start = [(2006 + 20/365.25) (2006 + (4/12))];
GEOS5247 = [(2006 + (4/12)) (2006 + (9/12) + (15/365.25))];
GEOA5 = [(2006 + (9/12) + (15/365.25)) (2009 + (6/12) + (7/365.25))]; % currently to start of S6
GEOS6 = [(2009 + (6/12) + (7/365.25)) 2012];

% TAMA data taking runs (DT1-9)
TAMADT1 = [(1999 + (7/12) + (6/365.25)) (1999 + (7/12) + (7/365.25))];
TAMADT2 = [(1999 + (8/12) + (17/365.25)) (1999 + (8/12) + (20/365.25))];
TAMADT3 = [(2000 + (3/12) + (20/365.25)) (2000 + (3/12) + (23/365.25))];
TAMADT4 = [(2000 + (7/12) + (21/365.25)) (2000 + (8/12) + (4/365.25))];
TAMADT5 = [(2001 + (2/12) + (2/365.25)) (2001 + (2/12) + (8/365.25))];
TAMADT6 = [(2001 + (7/12) + (0/365.25)) (2001 + (8/12) + (20/365.25))];
TAMADT7 = [(2002 + (7/12) + (31/365.25)) (2002 + (8/12) + (2/365.25))];
TAMADT8 = LIGOS2;
TAMADT9 = [(2003 + (10/12) + (28/365.25)) (2004 + 10/365.25)];

% VIRGO runs, weekend science run (WSR) and VSR1-4
VIRGOWSR = [(2006 + (8/12) + (8/365.25)) (2007 + (2/12) + (12/365.25))];
VIRGOVSR1 = [(2007 + (4/12) + (18/365.25)) (2007+(9/12))];
VIRGOA5 = [(2007+(9/12)) (2009 + (6/12) + (7/365.25))];
VIRGOVSR2 = [(2009 + (6/12) + (7/365.25)) (2010 + (8/365.25))];
VIRGOVSR3 = [(2010 + (7/12) + (11/365.25)) (2010 + (6/12) + (20/365.25))];
VIRGOVSR4 = [(2011 + (5/12) + (3/365.25)) (2011 + (8/12) + (5/365.25))]; 

% make plot (currently goes to 2012)
% draw some thin horozinatal lines for asthetics 
plot([1999 2012], [1 1], 'k--', 'linewidth', 0.5)
hold on
plot([1999 2012], [2 2], 'k--', 'linewidth', 0.5)
plot([1999 2012], [3 3], 'k--', 'linewidth', 0.5)
plot([1999 2012], [4 4], 'k--', 'linewidth', 0.5)

% plot LIGO
plot(LIGOS1, [1 1], 'm-o', LIGOS2, [1 1], 'm-o', LIGOS3, [1 1], 'm-o',...
    LIGOS4, [1 1], 'm-o', LIGOS5, [1 1], 'm-o', LIGOA5, [1 1], 'm--', ...
    LIGOS6, [1 1], 'm-o', 'linewidth', 3, 'markersize', 4);

% plot GEO
plot(GEOS1, [2 2], 'b-o', GEOS3I, [2 2], 'b-o', GEOS3II, [2 2], 'b-o',...
    GEOS4, [2 2], 'b-o', GEOS5start, [2 2], 'b--', GEOS5247, [2 2], ...
    'b-o', GEOA5, [2 2], 'b--o', GEOS6, [2 2], 'b-->', 'linewidth', 3, ...
    'markersize', 4);

% plot TAMA
plot(TAMADT1, [3 3], 'r-o', TAMADT2, [3 3], 'r-o',TAMADT3, [3 3], ...
    'r-o',TAMADT4, [3 3], 'r-o',TAMADT5, [3 3], 'r-o',TAMADT6, [3 3], ...
    'r-o',TAMADT7, [3 3], 'r-o',TAMADT8, [3 3], 'r-o',TAMADT9, [3 3], ...
    'r-o', 'linewidth', 3, 'markersize', 4);

% plot VIRGO
plot(VIRGOWSR, [4 4], 'g--', VIRGOVSR1, [4 4], 'g-o', ...
    VIRGOA5, [4 4], 'g--', ...
    VIRGOVSR2, [4 4], 'g-o', VIRGOVSR3, [4 4], 'g-o', ...
    VIRGOVSR4, [4 4], 'g-o', ...
    'linewidth', 3, 'markersize', 4);

% set y axis (0-5 to give a space at the top and bottom)
ylim([0 5]);

% add detector names to y axis
set(gca, 'ytick', [0 1 2 3 4 5], ...
    'yticklabel', {'', 'LIGO', 'GEO600', 'TAMA300', 'VIRGO', ''});

% set the x axis from 1999.5 to 2012 (can change)
xlim([1999.5 2012]);

% add tick marks every quarter year, but only label the years
set(gca, 'xtick', [1999.5 1999.75 2000 2000.25 2000.5 2000.75 2001 ...
    2001.25 2001.5 2001.75 2002 2002.25 2002.5 2002.75 2003 2003.25 ...
    2003.5 2003.75 2004 2004.25 2004.5 2004.75 2005 2005.25 2005.5 ...
    2005.75 2006 2006.25 2006.5 2006.75 2007 2007.25 2007.5 2007.75 ...
    2008 2008.25 2008.5 2008.75 2009 2009.25 2009.5 2009.75 2010 ...
    2010.25 2010.5 2010.75 2011 2011.25 2011.5, 2011.75, 2012], 'xticklabel', ...
    {'', '', 2000, '', '', ...
    '', 2001, '', '', '', 2002, '', '', '', 2003, '', '', '', 2004, '', ...
    '', '', 2005, '', '', '', 2006, '', '', '', 2007, '', '', '', 2008, ...
    '', '', '', 2009, '', '', '', 2010, '', '', '', 2011, '', '', '', 2012});

% turn the grid on
grid on

xlabel('Year');

% set the plot line thinkness to 1
set(gca, 'linewidth', 1);

hold off