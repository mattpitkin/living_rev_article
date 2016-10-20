% read in pulsar spin-down upper limits
[num, name, freqs, sdh, sde] = ...
    textread('sdlimits.txt', ...
    '%d%s%f%f%f');

% OPENGL CAN'T DO TRANSPARENCY IN LOG PLOTS SO I HAVE TO CONVERT EVERYTHING
% TO LOG10(val)

% plot spin-down limits
plot(log10(freqs), log10(sdh), 'kv', 'markersize', 9, 'markerfacecolor', [0 0 0]);
hold on;

% read in Enhanced LIGO curve
enligo = load('../EnhancedLIGO.txt');

% read in Virgo+ curve
vp = load('../VIRGOVSR2.txt');

% read in Advanced LIGO curve
al = load('../../advligo.txt');

% read in ET curve
load ../ET_sensitivity.mat

% create Enhanced LIGO SRD
tv = 365.25*86400; % 1 year integration for VSR2

clear invjoint joint lowlim upplim vals

% create joint sensitivity estimate
invjoint = ((tv./enligo(:,2).^2) + (tv./enligo(:,2).^2));
joint = 10.8*sqrt(1./invjoint);

% create VSR2 sensitivity estimate
invjointV = tv./vp(:,2).^2;
jointV = 10.8*sqrt(1./invjointV);

% create AdvLIGO sensitivity estimate
invjointAL = 3*((tv./al(:,2).^2));
jointAL = 10.8*sqrt(1./invjointAL);

% create ET sensitivity estimate
invjointET = ((tv./ET_strain(1:10:end).^2));

% find lower and upper bounds (estimated from fig 1 of Dupuis and Woan)
lowlim = log10(7*sqrt(1./invjoint));
upplim = log10(20*sqrt(1./invjoint));
vals = find(enligo(:,1) > 1 & enligo(:,1) <= 2000);

lowlimV = log10(7*sqrt(1./invjointV));
upplimV = log10(20*sqrt(1./invjointV));

lowlimA = log10(7*sqrt(1./invjointAL));
upplimA = log10(20*sqrt(1./invjointAL));

lowlimE = log10(7*sqrt(1./invjointET));
upplimE = log10(20*sqrt(1./invjointET));

% plot on top of other curve
h2 = patch([log10(enligo(vals,1)); log10(flipud(enligo(vals,1)))], ...
    [lowlim(vals); flipud(upplim(vals))], [0.3, 0.5, 0.7], 'edgecolor', ...
    'none', 'facealpha', 0.5);

% plot VSR2 curve on top
h3 = patch([log10(vp(:,1)); log10(flipud(vp(:,1)))], ...
    [lowlimV; flipud(upplimV)], [0.2, 0.7, 0.2], 'edgecolor', ...
    'none', 'facealpha', 0.5);

% plot AdvLIGO
h4 = patch([log10(al(:,1)); log10(flipud(al(:,1)))], ...
    [lowlimA; flipud(upplimA)], [0.5, 0.2, 0.35], 'edgecolor', ...
    'none', 'facealpha', 0.5);

% plot ET curve
h5 = patch([log10(freq(1:10:end)'); log10(flipud(freq(1:10:end)'))], ...
    [lowlimE'; flipud(upplimE')], [0.9, 0.4, 0.4], 'edgecolor', ...
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

legend('spin-down limits', ...
   'Enhanced LIGO S6', ...
   'Virgo+ VSR2', ...
   'Advanced LIGO', ...
   'Einstein Telescope');

xlim([0 log10(2000)]);
ylim([-28 -23]);
grid on

set(gca, 'linewidth', 1.5, 'fontsize', 24);

hold off

%a2 = loglog(ligo2k, joint, 'color', [0.3 0.5 0.7], 'linewidth', 10);