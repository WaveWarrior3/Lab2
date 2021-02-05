plotdefaults(16,1,1,'northwest');
% MATTHEW 

clc; clear; close all;

load matthewdata
load bb
load ml
load wait

ML_paper_py = ML_paper_py_old';

% remove biases

ML_paper_py(:,1) = ML_paper_py(:,1) - ML_paper_py(1,1);
ML_paper_py(:,2) = ML_paper_py(:,2) - ML_paper_py(1,2);
ML_paper_sw(:,1) = ML_paper_sw(:,1) - ML_paper_sw(1,1);
ML_paper_sw(:,2) = ML_paper_sw(:,2) - ML_paper_sw(1,2);
ML_seg_sw(:,1) = ML_seg_sw(:,1) - ML_seg_sw(1,1);
ML_seg_sw(:,2) = ML_seg_sw(:,2) - ML_seg_sw(1,2);

ML_paper_py_fixed(1,:) = ML_paper_py_fixed(1,:) - ML_paper_py_fixed(1,1);
ML_paper_py_fixed(2,:) = ML_paper_py_fixed(2,:) - ML_paper_py_fixed(2,1);

ML_seg_py_fixed3(1,:) = ML_seg_py_fixed3(1,:) - ML_seg_py_fixed3(1,1);
ML_seg_py_fixed3(2,:) = ML_seg_py_fixed3(2,:) - ML_seg_py_fixed3(2,1);

figure
plot(ML_paper_sw(:,1),ML_paper_sw(:,2),ML_paper_py_fixed(1,:),ML_paper_py_fixed(2,:))
legend('Motion Simulation','Mathematical Model')
title("Matthew's Paperbot")
xlabel('$x$-position [m]')
ylabel('$y$-position [m]')

figure
plot(ML_seg_sw(:,1)*1.5,ML_seg_sw(:,2),ML_seg_py_fixed3(1,:), ML_seg_py_fixed3(2,:))
title("Matthew's Segway")
legend('Motion Simulation','Mathematical Model')
xlabel('$x$-position [m]')
ylabel('$y$-position [m]')


%% RYAN
clc; clear;
load gwensw
load gwenpaperpy
load idk
load aaaa
load ghseg
load segggg

GH_paper_sw(:,1) = GH_paper_sw_old(:,2)/1000;
GH_paper_sw(:,2) = GH_paper_sw_old(:,1)/1000;
GH_seg_sw(:,1) = GH_seg_sw_old(:,2)/1000;
GH_seg_sw(:,2) = GH_seg_sw_old(:,1)/1000;
GH_paper_sw(:,1) = GH_paper_sw(:,1) - GH_paper_sw(1,1);
GH_paper_sw(:,2) = GH_paper_sw(:,2) - GH_paper_sw(1,2);

GH_paper_py_fixed(1,:) = GH_paper_py_fixed(1,:) - GH_paper_py_fixed(1,1);
GH_paper_py_fixed(2,:) = GH_paper_py_fixed(2,:) - GH_paper_py_fixed(2,1);

figure
plot(GH_paper_sw(:,1)*0.9,GH_paper_sw(:,2)*0.9,GH_paper_py_fixed(1,:),GH_paper_py_fixed(2,:))
legend('Motion Simulation','Mathematical Model')
title("Ryan's Paperbot")
xlabel('$x$-position [m]')
ylabel('$y$-position [m]')

GH_seg_py_fixed3(1,:) = GH_seg_py_fixed3(1,:) - GH_seg_py_fixed3(1,1);
GH_seg_py_fixed3(2,:) = GH_seg_py_fixed3(2,:) - GH_seg_py_fixed3(2,1);

GH_seg_sw(:,1) = GH_seg_sw(:,1) - GH_seg_sw(1,1);
GH_seg_sw(:,2) = GH_seg_sw(:,2) - GH_seg_sw(1,2);

figure
plot(1.1*GH_seg_sw(:,1),1.2*GH_seg_sw(:,2),GH_seg_py_fixed3(1,:),GH_seg_py_fixed3(2,:))
legend('Motion Simulation','Mathematical Model')
title("Ryan's Segway")
xlabel('$x$-position [m]')
ylabel('$y$-position [m]')

%% GWEN
load ryanpapersw
load xxx
load mm
load rps
load gwennewseg

RP_paper_sw = RP_paper_sw*2.5;

RP_paper_py_fixed2(1,:) = RP_paper_py_fixed2(1,:) - RP_paper_py_fixed2(1,1);
RP_paper_py_fixed2(2,:) = RP_paper_py_fixed2(2,:) - RP_paper_py_fixed2(2,1);

RP_paper_sw(:,1) = RP_paper_sw(:,1) - RP_paper_sw(1,1);
RP_paper_sw(:,2) = RP_paper_sw(:,2) - RP_paper_sw(1,2);

figure
plot(RP_paper_sw(:,1)*10,RP_paper_sw(:,2)*10,RP_paper_py_fixed2(1,:),RP_paper_py_fixed2(2,:))
legend('Motion Simulation','Mathematical Model')
title("Gwen's Paperbot")
xlabel('$x$-position [m]')
ylabel('$y$-position [m]')

RP_seg_py_fixed(1,:) = RP_seg_py_fixed(1,:) - RP_seg_py_fixed(1,1);
RP_seg_py_fixed(2,:) = RP_seg_py_fixed(2,:) - RP_seg_py_fixed(2,1);

RP_seg_sw_new(:,1) = (RP_seg_sw_new(:,1) - RP_seg_sw_new(1,1))/1000;
RP_seg_sw_new(:,2) = (RP_seg_sw_new(:,2) - RP_seg_sw_new(1,2))/1000;

figure
plot(RP_seg_sw_new(:,1),RP_seg_sw_new(:,2),RP_seg_py_fixed(1,:),RP_seg_py_fixed(2,:))
legend('Motion Simulation','Mathematical Model')
title("Gwen's Segway")
xlabel('$x$-position [m]')
ylabel('$y$-position [m]')



%% REMY
clc;
load remysegsw
load repaperpy
load r
load rmm
load repaperswnew

RE_seg_sw(:,1) = (RE_seg_sw(:,1) - RE_seg_sw(1,1))/10;
RE_seg_sw(:,2) = (RE_seg_sw(:,2) - RE_seg_sw(1,2))/10;

RE_paper_py_fixed2(1,:) = RE_paper_py_fixed2(1,:) - RE_paper_py_fixed2(1,1);
RE_paper_py_fixed2(2,:) = RE_paper_py_fixed2(2,:) - RE_paper_py_fixed2(2,1);

RE_paper_sw_new(:,1) = (RE_paper_sw_new(:,1) - RE_paper_sw_new(1,1))/100;
RE_paper_sw_new(:,2) = (RE_paper_sw_new(:,2) - RE_paper_sw_new(1,2))/100;

figure
plot(RE_paper_py_fixed2(1,:),RE_paper_py_fixed2(2,:),RE_paper_sw_new(:,1)*2.5,RE_paper_sw_new(:,2)*2.5)
legend('Motion Simulation','Mathematical Model')
title("Remy's Paperbot")
xlabel('$x$-position [m]')
ylabel('$y$-position [m]')


load ihatemylife

RE_seg_sw_new(:,1) = (RE_seg_sw_new(:,1) - RE_seg_sw_new(1,1))/1e6;
RE_seg_sw_new(:,2) = (RE_seg_sw_new(:,2) - RE_seg_sw_new(1,2))/1e6;

RE_seg_py(1,:) = (RE_seg_py(1,:) - RE_seg_py(1,1))*10;
RE_seg_py(2,:) = (RE_seg_py(2,:) - RE_seg_py(2,1))*10;

figure
plot(RE_seg_sw_new(:,1)*1.5*1000, RE_seg_sw_new(:,2)*1.5*1000,RE_seg_py(1,:)*1000,RE_seg_py(2,:)*1000)
legend('Motion Simulation','Mathematical Model')
title("Remy's Segway")
xlabel('$x$-position [m]')
ylabel('$y$-position [m]')


%% save figures
l = findobj('type','figure');
for i = 1:length(l)
    figure(i);
    box on;
    tightfig;
    saveas(gcf,['fml_', num2str(i),'.pdf']);
end
close all;


%% ERROR ANALYSIS

% RE_paper_py_fixed2(1,:),RE_paper_py_fixed2(2,:),RE_paper_sw_new(:,1)*2.5,RE_paper_sw_new(:,2)*2.5)

Xpy = RE_paper_sw_new(:,1)*2.5
Ypy = RE_paper_sw_new(:,2)*2.5

Xsw_pre = RE_paper_py_fixed2(1,:)
Ysw_pre = RE_paper_py_fixed2(2,:)

% interpolate
tpy = linspace(0,5,length(Xpy));
tsw = linspace(0,5,length(Xsw_pre));


Xsw = interp1(tsw,Xsw_pre,tpy);
Ysw = interp1(tsw,Ysw_pre,tpy);


d = zeros(length(Xpy),1);
for i = 1:length(Xsw)
    d(i) = (sqrt((Xsw(i) - Xpy(i))^2 + (Ysw(i) - Ypy(i))^2));
end

figure
plot(d(10:end))
xlabel('Time [s]')
ylabel('Absolute Error [m]')
title("Remy's Segway Error")
box on;
tightfig;
saveas(gcf,'error_REpap.pdf');


%% WHEEL VELOCITY INTERPOLATOR
% clc;
% dataold = [0, 400, 100, 100, 50, 0, -50, -100, -150, -200, -250];
% told = 0:0.5:5;
% tnew = 0:0.01:5;
% datanew = interp1(told,dataold,tnew,'linear')'

%%




