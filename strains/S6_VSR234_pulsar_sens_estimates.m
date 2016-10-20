% script to estimate upper limits for known pulsars with S6/VSR2/3/4

% detector duty cycles (approximate - from science segment lists)
S6H1duty = 20072626; % seconds
S6L1duty = 18977473;
VSR2duty = 12666643;
VSR3duty = 4272248;
VSR4duty = 6627226;

% get approximate sensitivity curves
H1sens = load('/home/matthew/analyses/strains/S6/lho4k_100222_strain.txt');
L1sens = load('/home/matthew/analyses/strains/S6/llo4k_100220_strain.txt');
VSR2sens = load('/home/matthew/analyses/strains/S6/SensitivityH_VSR2_091020.txt');
VSR3sens = load('/home/matthew/analyses/strains/S6/Sensitivity_VSR3_20100916_5Mpc.txt');
VSR4sens = load('/home/matthew/analyses/strains/S6/Sensitivity_VSR4_20110805_11d8Mpc.txt');

% interpolate frequencies onto new scale
fs = 5:0.05:2000;

H1int = interp1(H1sens(:,1), H1sens(:,2), fs, 'spline');
L1int = interp1(L1sens(:,1), L1sens(:,2), fs, 'spline');
VSR2int = interp1(VSR2sens(:,1), VSR2sens(:,2), fs, 'spline');
VSR3int = interp1(VSR3sens(:,1), VSR3sens(:,2), fs, 'spline');
VSR4int = interp1(VSR4sens(:,1), VSR4sens(:,2), fs, 'spline');

% sum PSDs in quadrature to get h0 senstivity estimate
ulest = 10.8*sqrt(1./( (S6H1duty./(H1int.^2)) + ...
    (S6L1duty./(L1int.^2)) + (VSR2duty./(VSR2int.^2)) + ...
    (VSR3duty./(VSR3int.^2)) + (VSR4duty./(VSR4int.^2))));

% get pulsars (all non-GC pulsars) - file contains:
% # GW freq, h0 spin-down limit, ellipticity spin-down limit
%pulsars = load('/home/matthew/analyses/strains/S6/pulsars.txt');
% no., name, spin-freq, fdot, h0 spin-down limit
fp = fopen('pulsars_S6VSR.txt', 'r');
C = textscan(fp, '%d%s%f%f%f');
fclose(fp);

% get pulsars with GW f > 20 Hz;
vals = find(2*C{3}(:) > 20 & C{5}(:) ~= 0);

pfs = 2*C{3}(vals);
psds = C{5}(vals);

% get estimate of 95% upper limit sensitivity for each pulsar and compare 
% with spin-down
pulests = zeros(length(vals), 1);
psdrats = zeros(length(vals), 1);
for i=1:length(vals)
    posf = round((pfs(i) - fs(1))/(fs(2)-fs(1)));
    pulests(i) = ulest(posf);
    psdrats(i) = ulest(posf)/psds(i);
end

figure
loglog(fs, ulest, 'b', pfs, pulests, 'rx');
xlim([fs(1) fs(end)]);
xlabel('Frequency (Hz)', 'fontname', 'avantgarde', 'fontsize', 14');
ylabel('Strain', 'fontname', 'avantgarde', 'fontsize', 14');
set(gca, 'fontname', 'helvetica', 'fontsize', 16, 'linewidth', 1.5);
grid on;

figure
loglog(pfs, psdrats, 'rx');
xlim([fs(1) fs(end)]);
xlabel('Frequency (Hz)', 'fontname', 'avantgarde', 'fontsize', 14');
ylabel('Spin-down ratio', 'fontname', 'avantgarde', 'fontsize', 14');
set(gca, 'fontname', 'helvetica', 'fontsize', 16, 'linewidth', 1.5);
grid on;