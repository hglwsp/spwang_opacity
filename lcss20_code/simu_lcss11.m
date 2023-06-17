...
clc; clear; close all;
echo on;
%% Parameters
% 2-dimensional system
% x(t+1) = x(t) + v(t) + 0.5*u(t); v(t+1) = v(t) + u(t); y(t) = v(t)
A = [1 1; 0 1];
B = [0.5; 1];
C = [0 1];

% 
c = 1;
delta = 2;
epsilon_1 =1;
epsilon_2 =1.001;  % epsilon_2 >= epsilon_1
kappa = 1 ;     % constant kappa in the last condition

%% SOS Program
% define variables required for SOS program
syms x1 x2 v1 v2 k1 k2 u1;
vars = [x1; x2; v1; v2;u1];

% define lower and upper bounds
X_min = [0; 0];
X_max = [4; 4];
X_0_min = X_min;
X_0_max = X_max;
X_s_min = [0; 0];
X_s_max = [0.8; 0.8];
X_ns_min = [0.8; 0.8];
X_ns_max = [4; 4];
V_min = [0; 0];
V_max = [0.1; 0.1]; 
K_min = [0; 0];
K_max = [0.5; 0.5];
U_min = [0.03; 0.03];
U_max = [0.05; 0.05]; 


% control region
U1_all = (u1-U_min(1))*(U_max(1)-u1);

% all region
X1_all = (x1-X_min(1))*(X_max(1)-x1);
X2_all = (x2-X_min(2))*(X_max(2)-x2);
X_all  = [X1_all; X2_all];    
V1_all = (v1-V_min(1))*(V_max(1)-v1);
V2_all = (v2-V_min(2))*(V_max(2)-v2); 
V_all  = [V1_all; V2_all];
K1_all = (k1-K_min(1))*(K_max(1)-k1);
K2_all = (k2-K_min(2))*(K_max(2)-k2); 
K_all  = [K1_all; K2_all];

% initial region
% The polynomial functions for defining the semialgebraic region R_0(X_initial here);
% g_01 = (x1-X_s_min(1))*(X_s_max(1)-x1); 
% g_02 = (x2-X_ns_min(2))*(X_ns_max(2)-x2);
% g_03 = -(c*x1-c*x2)^2+delta^2;
% g_04 = V1_all;
% g_05 = V2_all;
% g_0  = [g_01; g_02; g_03; g_04; g_05];
% 
% % unsafe region
% % The polynomial functions for defining the semialgebraic region R_u(X_unsafe here);
% g_u1 = (x1-X_min(1))*(X_max(1)-x1); 
% g_u2 = (x2-X_min(2))*(X_max(2)-x2);
% g_u3 = (c*x1-c*x2)^2-delta^2-0.01;
% g_u4 = V1_all;
% g_u5 = V2_all;
% g_u  = [g_u1; g_u2; g_u3; g_u4; g_u5];


nr_time = 300;
nr_iter = 30;

x1_traj = NaN(nr_iter, nr_time);
x2_traj = NaN(nr_iter, nr_time);
v1_traj = NaN(nr_iter, nr_time);
v2_traj = NaN(nr_iter, nr_time);
k1_traj = NaN(nr_iter, nr_time);
k2_traj = NaN(nr_iter, nr_time);
u1_traj = NaN(nr_iter, nr_time);
u2_traj = NaN(nr_iter, nr_time);
% % bc = NaN(nr_iter, nr_time);
% % bc_diff = NaN(nr_iter, nr_time);


% show results
% Barrier_function =  0.2354*v1^2 - 0.4709*v1*v2 + 0.005946*v1*x1 - 0.005947*v1*x2 + 4.051e-5*v1 + 0.2354*v2^2 
% - 0.00595*v2*x1 + 0.005948*v2*x2 + 5.357e-5*v2 + 0.9239*x1^2 - 1.848*x1*x2 - 7.712e-5*x1 + 0.9239*x2^2 
% - 0.000111*x2 + 0.07164;
% bc_fh = matlabFunction(Barrier_function, 'Vars', [x1,x2,v1,v2]);

for i_iter = 1: nr_iter
    % generate initial state randomly
    x1_0 = (X_s_max(1)-X_s_min(1)).*rand(1) + X_s_min(1);
    x2_0 = 1.0416*x1_0*x1_0*x1_0 - 0.2083*x1_0*x1_0 + 0.25 * x1_0 + 0.9;
    while (-(c*x1_0-c*x2_0)^2+(delta)^2 < 0)
        x1_0 = (X_s_max(1)-X_s_min(1)).*rand(1) + X_s_min(1);
        x2_0 = 1.0416*x1_0*x1_0*x1_0 - 0.2083*x1_0*x1_0 + 0.25 * x1_0 + 0.9;
    end
%     
    v1_0 = (V_max(1)-V_min(1)).*rand(1) +V_min(1);
    v2_0 = (V_max(1)-V_min(1)).*rand(1) +V_min(1);
    k1_0 = (K_max(1)-K_min(1)).*rand(1) +K_min(1);
    k2_0 = (K_max(1)-K_min(1)).*rand(1) +K_min(1);

%     v1_0 = 0.1;
%     v2_0 = 0.1;
%     k1_0 = 0.1;
%     k2_0 = 0.1;
    x1_traj(i_iter, 1) = x1_0;
    x2_traj(i_iter, 1) = x2_0;
    v1_traj(i_iter, 1) = v1_0;
    v2_traj(i_iter, 1) = v2_0;
    k1_traj(i_iter, 1) = k1_0;
    k2_traj(i_iter, 1) = k2_0;

        
    % define dynamics x(k+1)=f(x(k),w(k))
    for i_time = 1: nr_time

        u1_t = (U_max(1)-U_min(1)).*rand(1) + U_min(1);
        x1_t = x1_traj(i_iter, i_time) + 0.5*v1_traj(i_iter, i_time)+k1_traj(i_iter, i_time) + 0.5*u1_t;
        v1_t =  v1_traj(i_iter, i_time)  + 0.5*u1_t;
        k1_t = 0.2*k1_traj(i_iter, i_time)*k1_traj(i_iter, i_time)*k1_traj(i_iter, i_time) + 0.05*u1_t;
        

        if u1_t  >= U_max(1)
            u1_t = U_max(1);
        end
        if u1_t  <= U_min(1)
            u1_t = U_min(1);
        end
        
        if x1_t >= X_max(1)
            x1_t = X_max(1);
        end
        if v1_t >= V_max(1)
            v1_t = V_max(1);
        end
        if k1_t >= K_max(1)
            k1_t = K_max(1);
        end
        if x1_t <= X_min(1)
            x1_t = X_min(1);
        end
        if v1_t <= V_min(1)
            v1_t = V_min(1);
        end
        if k1_t <= K_min(1)
            k1_t = K_min(1);
        end

        u2_t = 0.690012174927933*relu(-2.43972461147879*x1_traj(i_iter, i_time) - 1.72369459490275*x2_traj(i_iter, i_time) - 0.747375004375506*v1_traj(i_iter, i_time) - 1.02999123525472*v2_traj(i_iter, i_time) - 1.26939757544406*k1_traj(i_iter, i_time) - 1.33519022599*k2_traj(i_iter, i_time) + 1.20692396476145*u1_t - 0.691681803052652)...
            - 1.7279258914598*relu(-1.23384203453083*x1_traj(i_iter, i_time) - 0.699207950957716*x2_traj(i_iter, i_time) + 2.73849844272985*v1_traj(i_iter, i_time) + 0.0738675079630652*v2_traj(i_iter, i_time) - 0.310551611413362*k1_traj(i_iter, i_time) - 0.659599872190942*k2_traj(i_iter, i_time) - 0.207757946870372*u1_t - 0.287144124662645)...
            + 0.000200492374993064*relu(-0.949063399238092*x1_traj(i_iter, i_time) - 0.310559323487395*x2_traj(i_iter, i_time) - 1.72651695914931*v1_traj(i_iter, i_time)- 0.172087992047418*v2_traj(i_iter, i_time)- 0.801657076201584*k1_traj(i_iter, i_time) + 0.542632919252449*k2_traj(i_iter, i_time) - 0.652256803452039*u1_t + 0.788084695706705)...
            - 0.0115004780871159*relu(-0.114309017806746*x1_traj(i_iter, i_time) - 0.115573811307475*x2_traj(i_iter, i_time) + 0.0337738583398876*v1_traj(i_iter, i_time) - 0.650364139301828*v2_traj(i_iter, i_time) + 1.5517702695048*k1_traj(i_iter, i_time)- 1.48367948197577*k2_traj(i_iter, i_time) - 0.923248178625012*u1_t + 0.229185546216994)...
            - 2.27264421623864*relu(0.0100469041511025*x1_traj(i_iter, i_time) - 2.06781397201443*x2_traj(i_iter, i_time) + 0.457901652479034*v1_traj(i_iter, i_time) - 0.120592294583022*v2_traj(i_iter, i_time) + 0.305363553681167*k1_traj(i_iter, i_time)- 1.94942713843718*k2_traj(i_iter, i_time) + 0.661871851377484*u1_t - 0.132955283933316)...
            - 0.0411949618749434*relu(0.0294888755063933*x1_traj(i_iter, i_time) - 0.0120001554938917*x2_traj(i_iter, i_time) - 0.376583236679991*v1_traj(i_iter, i_time) + 0.0470403447233036*v2_traj(i_iter, i_time) + 0.88621896769657*k1_traj(i_iter, i_time) - 0.550525948423665*k2_traj(i_iter, i_time) - 0.92659602837582*u1_t - 0.0769745266091512)...
            - 0.0451605157358305*relu(0.251770591174538*x1_traj(i_iter, i_time) + 0.0854224352646429*x2_traj(i_iter, i_time) - 0.238716678181958*v1_traj(i_iter, i_time) + 1.60145779763594*v2_traj(i_iter, i_time) - 1.94356467279984*k1_traj(i_iter, i_time) + 1.8610449122718*k2_traj(i_iter, i_time) - 0.837681260804344*u1_t- 1.38110004186867)...
            - 1.6165150481094*relu(0.263503815150707*x1_traj(i_iter, i_time) - 0.405506948794891*x2_traj(i_iter, i_time) + 0.35796098591317*v1_traj(i_iter, i_time) + 1.17030246893884*v2_traj(i_iter, i_time)+ 0.460255292642808*k1_traj(i_iter, i_time) + 0.00273344800799369*k2_traj(i_iter, i_time)- 1.02836703828054*u1_t - 1.24875541376093)...
            + 0.0494335430001635
%         u2_t = 0.0916155710042751*relu(-1.4556321910415*x1_traj(i_iter, i_time) - 0.352980668928574*x2_traj(i_iter, i_time) - 1.13146648391901*v1_traj(i_iter, i_time) + 0.0170196009907576*v2_traj(i_iter, i_time) + 0.556460454064127*k1_traj(i_iter, i_time) + 0.302375709093136*k2_traj(i_iter, i_time) + 0.122363544701346*u1_t + 0.025594342506373)...
%             - 0.079988658745984*relu(-1.07040884531335*x1_traj(i_iter, i_time) - 0.310931871295977*x2_traj(i_iter, i_time) + 1.16056454516844*v1_traj(i_iter, i_time) - 1.94739630724454*v2_traj(i_iter, i_time) + 0.624632019558321*k1_traj(i_iter, i_time) + 0.123650421879396*k2_traj(i_iter, i_time) - 1.5856538498229*u1_t- 0.268537498546241) ...
%             + 0.98773093337398*relu(-0.469171724656549*x1_traj(i_iter, i_time) - 1.22865139838854*x2_traj(i_iter, i_time) - 0.558409775528439*v1_traj(i_iter, i_time) + 0.579205853262753*v2_traj(i_iter, i_time) - 0.552473112147244*k1_traj(i_iter, i_time) + 0.846101390583569*k2_traj(i_iter, i_time) - 2.22188653775783*u1_t - 0.891554727056855)...
%             + 0.028858004205528*relu(-0.325890115114594*x1_traj(i_iter, i_time) + 0.213158768812746*x2_traj(i_iter, i_time) + 0.355082931723485*v1_traj(i_iter, i_time) + 0.0797964290350801*v2_traj(i_iter, i_time) + 0.48182070025426*k1_traj(i_iter, i_time) + 1.65233588885806*k2_traj(i_iter, i_time) - 1.11038691692783*u1_t - 0.911562144988182)...
%             + 0.00188541104043506*relu(-0.202159642682815*x1_traj(i_iter, i_time) - 0.137921516351718*x2_traj(i_iter, i_time) - 0.416529427440337*v1_traj(i_iter, i_time) + 0.448741539982331*v2_traj(i_iter, i_time) - 0.87051113720164*k1_traj(i_iter, i_time) + 0.135099702255136*k2_traj(i_iter, i_time) - 0.595410195125702*u1_t + 0.432885180861654)...
%             + 0.0325537091166759*relu(0.0761480707205186*x1_traj(i_iter, i_time) + 0.0984524922544578*x2_traj(i_iter, i_time) + 1.3915146188536*v1_traj(i_iter, i_time) + 1.13801748860301*v2_traj(i_iter, i_time) + 1.29411636934906*k1_traj(i_iter, i_time) - 1.54163522530528*k2_traj(i_iter, i_time) - 0.515323139266206*u1_t - 0.789174524679947)...
%             + 0.000453846319540884*relu(0.396231610427764*x1_traj(i_iter, i_time) - 0.492776430479109*x2_traj(i_iter, i_time) + 2.1465367444433*v1_traj(i_iter, i_time) - 0.93934913171563*v2_traj(i_iter, i_time) + 0.349835809333761*k1_traj(i_iter, i_time) - 0.525778407638624*k2_traj(i_iter, i_time)- 1.74737865171736*u1_t - 1.39977308952442)...
%             + 0.00278478320923985*relu(0.397664999343903*x1_traj(i_iter, i_time) - 0.163104358965678*x2_traj(i_iter, i_time) - 0.00806754477125167*v1_traj(i_iter, i_time) + 2.45674411146597*v2_traj(i_iter, i_time) + 0.00337918072826432*k1_traj(i_iter, i_time)- 0.193068557978384*k2_traj(i_iter, i_time) - 1.08840148353891*u1_t - 1.39791710938014)...
%             - 0.0470073028256833

    
        if u2_t  >= U_max(1)
            u2_t = U_max(1);
        end
        if u2_t  <= U_min(1)
            u2_t = U_min(1);
        end
%         
        x2_t = x2_traj(i_iter, i_time) + 0.5*v2_traj(i_iter, i_time)+k2_traj(i_iter, i_time) + 0.5*u2_t;
        v2_t =  v2_traj(i_iter, i_time)  + 0.5*u2_t;
        k2_t = 0.2*k2_traj(i_iter, i_time)*k2_traj(i_iter, i_time)*k2_traj(i_iter, i_time) + 0.05*u2_t;  
        
        if x2_t >= X_max(1)
            x2_t = X_max(1);
        end
        if v2_t >= V_max(1)
            v2_t = V_max(1);
        end
        if k2_t >= K_max(1)
            k2_t = K_max(1);
        end
        if x2_t <= X_min(1)
            x2_t = X_min(1);
        end
        if v2_t <= V_min(1)
            v2_t = V_min(1);
        end  
        if k2_t <= K_min(1)
            k2_t = K_min(1);
        end
%         bc(i_iter, i_time+1) = bc_fh(x1_t,x2_t,v1_t,v2_t);
%         bc_diff(i_iter, i_time)= bc(i_iter, i_time+1)-bc(i_iter, i_time);
        % dS1 & dS2
        x1_traj(i_iter, i_time+1) = x1_t;
        x2_traj(i_iter, i_time+1) = x2_t;
        v1_traj(i_iter, i_time+1) = v1_t;
        v2_traj(i_iter, i_time+1) = v2_t;
        k1_traj(i_iter, i_time+1) = k1_t;
        k2_traj(i_iter, i_time+1) = k2_t;
        u1_traj(i_iter, i_time) = u1_t;
        u2_traj(i_iter, i_time) = u2_t;        
    end
 end
%%
%%
figure(1)
set(gcf, 'Position', [200, 200, 355, 350]);
my_color = get(gca, 'colororder');
nr_color = size(my_color, 1);
hold on; grid on; box on;

fill([0 1.8 0],[2.2 4 4],'c','facealpha',0.2,'edgealpha',0);
fill([2.2 4 4],[0 1.8 0],'c','facealpha',0.2,'edgealpha',0);

for i_iter = 1: nr_iter
    plot(x1_traj(i_iter, 1), x2_traj(i_iter, 1), '*', 'color', my_color(mod(i_iter, nr_color)+1, :));
  %    plot(x1_traj(i_iter, :), x2_traj(i_iter, :), 'color', my_color(mod(i_iter, nr_color)+1, :), 'LineWidth',2,'marker', 'o','MarkerSize',2);
  plot(x1_traj(i_iter, :), x2_traj(i_iter, :), 'color', my_color(mod(i_iter, nr_color)+1, :), 'LineWidth',1.5);
end
% plot([X_s_min(1) X_s_max(1)],[X_ns_min(2) X_s_max(1)], 'LineWidth',2, 'color', my_color(5, :));
% plot([X_s_max(1) X_s_max(1)],[X_s_max(1) (c*X_ns_min(1)+delta)/c], 'LineWidth',2, 'color', my_color(5, :));
% plot([X_s_min(1) X_s_max(1)],[X_ns_min(2) (c*X_ns_min(1)+delta)/c], 'LineWidth',2, 'color', my_color(5, :));
% fill([4 4.8 4.8 4 4],[4.8 4.8 5.55 4.85 4.8],'r','facealpha',0.2,'edgealpha',0);
plot([0 0.8 0.8 0 0 ],[0.8 0.8 3 2.2 0.8], 'LineWidth',1, 'color','k');axis([X_min(1) X_max(1) X_min(1) X_max(1)]);
axis square;
set(gca,'DataAspectRatio',[1 1 1],'Fontname','Arial');
set(gca, 'FontSize', 11,'Fontname','Arial');
xlabel('$x_1$', 'Interpreter', 'latex', 'FontSize',12,'Fontname','Arial');
ylabel('$\hat x_1$', 'Interpreter', 'latex', 'FontSize',12,'Fontname','Arial');

% legend(my_legend, 'Location', 'SE', 'Interpreter', 'latex', 'FontSize',11)
FcnRemoveWhiteSpace(gcf,gca);

% enlarged details
figure(2)
set(gcf, 'Position', [400, 400, 355, 350]);
my_color = get(gca, 'colororder');
nr_color = size(my_color, 1);
hold on; grid on; box on;
for i_iter = 1: nr_iter
     plot(x1_traj(i_iter, 1), x2_traj(i_iter, 1), '*', 'color', my_color(mod(i_iter, nr_color)+1, :));  %  plot(x1_traj(i_iter, :), x2_traj(i_iter, :), 'color', my_color(mod(i_iter, nr_color)+1, :), 'LineWidth',2,'marker', 'o','MarkerSize',2);
%      plot(x12_traj(i_iter, :), x22_traj(i_iter, :), 'color', my_color(mod(i_iter, nr_color)+1, :), 'LineWidth',1);
end
fill([4 4.8 4.8 4 4],[4 4 4.8 4.8 4],'y','facealpha',0.2,'edgealpha',0);
fill([4 4.8 4.8 4],[4.85 5.65 6 6],'y','facealpha',0.2,'edgealpha',0);
fill([4 4.8 4.8 4 4],[4.8 4.8 5.65 4.85 4.8],'r','facealpha',0.2,'edgealpha',0);
plot([4 4.8 4.8 4 4],[4.8 4.8 5.65 4.85 4.8], 'LineWidth',1, 'color','r');
plot([4 4.8 4.8 4 4],[4.8 4.8 6 5.2 4.8], 'LineWidth',1, 'color','g');
axis([4 4.8 4 6]);
axis square;
set(gca,'DataAspectRatio',[1 1 1]);
set(gca, 'Fontname', 'Times New Roman', 'FontSize', 11);
xlabel('$x_{1}$', 'Interpreter', 'latex', 'FontSize',12);
ylabel('$\hat x_{1}$', 'Interpreter', 'latex', 'FontSize',12);
% legend(my_legend, 'Location', 'SE', 'Interpreter', 'latex', 'FontSize',11)
FcnRemoveWhiteSpace(gcf,gca);
%printpdf(gcf, 'ex1_200818');
%print('ex1_200818.emf','-dmeta','-r600');
%%
% figure(2);
% plot([1:nr_time],x1_traj(1:nr_time),'--r');
% hold on;
% plot([1:nr_time],x2_traj(1:nr_time),'b');
% hold on;
% plot([1:nr_time],(x1_traj(1:nr_time)-x2_traj(1:nr_time)),'g');
% legend('x_1','x_2');
% max(x1_traj-x2_traj)
% min(x1_traj-x2_traj)

% xlswrite('D:\pythonProject\opacity_loss1u\plot_traj\data_x1.xlsx',x1_traj)
% xlswrite('D:\pythonProject\opacity_loss1u\plot_traj\data_x2.xlsx',x2_traj)










