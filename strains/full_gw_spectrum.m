% m file to generate a plot containing all interferometers and source
% amplitude ranges

% load noise spectra
ligo4k = load('strains/LIGO_4k_SRD.txt');
advligo = load('AdvLIGO_ZERO_DET_high_P.txt');
et = load('ET_D_data.txt');
lisa = load('lisa.txt');

cpta = [ 137 144 160 179 201 231; 126 149 172 165 152 130 ]';
ska = [ 140 145 163 185 231 ; 163 196 238 226 200 ]';

ptaorigin = [80 87];
ptaoriginreal  = [-10 -10];

dx = (122-80);
dy = (116-87);

cpta(:,1) = ((cpta(:,1)-ptaorigin(1))/dx)+ptaoriginreal(1);
cpta(:,1) = 10.^cpta(:,1);

cpta(:,2) = ((ptaorigin(2)-cpta(:,2))/dy)+ptaoriginreal(2);
cpta(:,2) = 10.^cpta(:,2);

ska(:,1) = ((ska(:,1)-ptaorigin(1))/dx)+ptaoriginreal(1);
ska(:,1) = 10.^ska(:,1);

ska(:,2) = ((ptaorigin(2)-ska(:,2))/dy)+ptaoriginreal(2);
ska(:,2) = 10.^ska(:,2);

df = linspace(1e-3, 1e2, 10000);
fp = 7.36;
decigo = 6.53e-49*(1+(df/fp).^2) + ...
    4.45e-51*(df/1).^(-4).*(1+(df/fp).^2).^(-1) + ...
    4.94e-52*(df/1).^(-4);
decigo = sqrt(decigo);

bbo = 2.00e-49*(df/1).^2 + 4.58e-49 + 1.26e-52*(df/1).^(-4);
bbo = sqrt(bbo);

auriga = [ 907 920 937; 5e-21 4.2e-22 5e-21 ]';

% plot sensitivity curves
loglog(ligo4k(25:end,1), ligo4k(25:end,2), 'b', 'LineWidth', 2)
grid on;
hold on

loglog(advligo(:,1), advligo(:,2), 'b--', 'LineWidth', 2)
loglog(et(:,1), et(:,4), 'k', 'LineWidth', 2)
loglog(auriga(:,1), auriga(:,2), 'c', 'LineWidth', 2)
loglog(lisa(:,1), lisa(:,2), 'm', 'LineWidth', 2)
loglog(df, decigo, 'g', 'LineWidth', 2);
loglog(df, bbo, 'g--', 'LineWidth', 2);
loglog(cpta(:,1), cpta(:,2), 'r', 'LineWidth', 2)
loglog(ska(:,1), ska(:,2), 'r--', 'LineWidth', 2)
xlim([1e-9 10000])
legend('Initial LIGO', 'Advanced LIGO', 'Einstein Telescope', ...
    'AURIGA/ALLEGRO/NAUTILUS', ...
    'LISA', 'DECIGO', 'BBO', ... 
    'Pulsar Timing Array (Current)', 'Pulsar Timing Array (SKA)');
hold off

% Create xlabel
xlabel('Frequency (Hz)','FontSize',20,'FontName','helvetica');

% Create ylabel
ylabel('amplitude spectral density (strain Hz^{-1/2})','FontSize',20,...
    'FontName','helvetica');

set(gca, 'LineWidth',2, 'FontSize',19, 'FontName','helvetica', ...
    'xminortick', 'on', 'yminortick', 'on');