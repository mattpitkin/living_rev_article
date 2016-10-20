% read in pulsar spin-down upper limits
[num, name, freq, sdh, sde] = ...
    textread('sdlimits.txt', ...
    '%d%s%f%f%f');

% OPENGL CAN'T DO TRANSPARENCY IN LOG PLOTS SO I HAVE TO CONVERT EVERYTHING
% TO LOG10(val)

% plot spin-down limits
plot(log10(freq), log10(sdh), 'kv', 'markersize', 9, 'markerfacecolor', [0 0 0]);
hold on;

% set integration times for each pulsar
th1 = 527 * 86400; % seconds
th2 = 535 * 86400;
tl1 = 405 * 86400;

% read in S5 strain curves
lho4k = load('lho4k_070318_strain.txt');
lho2k = load('lho2k_070514_strain.txt');
llo4k = load('llo_060604_strain.txt');

% read in SRD curves
%ligo4k = load('../LIGO_4k_SRD.txt');
%ligo2k = load('../LIGO_2k_SRD.txt');

% read in Enhanced LIGO curve
enligo = load('../EnhancedLIGO.txt');

% read in Virgo+ curve
vp = load('../VIRGOVSR2.txt');

% interpolate 4k SRD to same as 2k
%ligo4kint(:,1) = ligo2k(:,1);
%ligo4kint(:,2) = interp1(ligo4k(:,1), ligo4k(:,2), ligo4kint(:,1));

% create S5 joint sensitivity estimates
invjoint = ((th1./lho4k(:,2).^2) + (tl1./llo4k(:,2).^2) +...
    (th2./lho2k(:,2).^2));
joint = 10.8*sqrt(1./invjoint);

% find lower and upper bounds (estimated from fig 1 of Dupuis and Woan)
lowlim = log10(7*sqrt(1./invjoint));
upplim = log10(20*sqrt(1./invjoint));

% find data between 20 Hz and 2000 Hz
vals = find(lho4k(:,1) > 20 & lho4k(:,1) < 2000);

% plot area
h = patch([log10(lho4k(vals,1)); log10(flipud(lho4k(vals,1)))], ...
    [lowlim(vals); flipud(upplim(vals))], [0.5, 0.5, 0.5], 'edgecolor', ...
    'none', 'facealpha', 0.7);

% plot mean sensitivity
grid on
%set(gca, 'xscale', 'log', 'yscale', 'log', 
set(gca, 'linewidth', 1.5, 'fontsize', 24, 'fontname', 'times')
%a = loglog(lho4k(:,1), joint, 'color', [0.8 0.8 0.8], 'linewidth', 10);
ylim([-27 -23]);

% create Enhanced LIGO SRD
% use same integration times as S5
%th1 = 365.25*86400;
%tl1 = 365.25*86400;
tv = 365.25*86400; % 1 year integration for VSR2

clear invjoint joint lowlim upplim vals

% create joint sensitivity estimate
invjoint = ((th1./enligo(:,2).^2) + (tl1./enligo(:,2).^2));
joint = 10.8*sqrt(1./invjoint);

% create VSR2 sensitivity estimate
invjointV = tv./vp(:,2).^2;
jointV = 10.8*sqrt(1./invjointV);

% find lower and upper bounds (estimated from fig 1 of Dupuis and Woan)
lowlim = log10(7*sqrt(1./invjoint));
upplim = log10(20*sqrt(1./invjoint));
vals = find(enligo(:,1) > 20 & enligo(:,1) <= 2000);

lowlimV = log10(7*sqrt(1./invjointV));
upplimV = log10(20*sqrt(1./invjointV));

% plot on top of other curve
h2 = patch([log10(enligo(vals,1)); log10(flipud(enligo(vals,1)))], ...
    [lowlim(vals); flipud(upplim(vals))], [0.3, 0.5, 0.7], 'edgecolor', ...
    'none', 'facealpha', 0.5);

% plot VSR2 curve on top
h3 = patch([log10(vp(:,1)); log10(flipud(vp(:,1)))], ...
    [lowlimV; flipud(upplimV)], [0.2, 0.7, 0.2], 'edgecolor', ...
    'none', 'facealpha', 0.5);

% set tick marks
yvals = log10(1e-27:1e-27:9e-27);
yvals = [yvals, log10(1e-26:1e-26:9e-26)];
yvals = [yvals, log10(1e-25:1e-25:9e-25)];
yvals = [yvals, log10(1e-24:1e-24:1e-23)];
set(gca, 'ytick', yvals, 'yticklabel', {'-27','','','','','','','',...
    '','-26','','','','','','','','','-25','','','','','','','',...
    '','-24','','','','','','','','','-23'});

xvals = [log10(1:1:9), log10(10:10:90), ...
    log10(100:100:900), log10(1000:1000:10000)];
set(gca, 'xtick', xvals, 'xticklabel', {'1','','','','','','','','',...
    '10','','','','','','','','','100','','','','','','','','',...
    '1000','','','','','','','','','10000'});

xlabel('frequency (Hz)', 'fontsize', 24, 'fontname', 'times');
ylabel('log_{10}\it{h_0}', 'fontsize', 24, 'fontname', 'times');

legend('spin-down limits', 'LIGO S5 joint sensitivity estimate',...
   'LIGO S6 joint sensitivity estimate', ...
   'Virgo VSR2 sensitivity estimate');

xlim([1 log10(2000)]);

hold off

%a2 = loglog(ligo2k, joint, 'color', [0.3 0.5 0.7], 'linewidth', 10);