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
pi = 3.14;
delta = pi/6;
g = 9.8;
epsilon_1 =1;
epsilon_2 =1.001;  % epsilon_2 >= epsilon_1
kappa = 1 ;     % constant kappa in the last condition


%% SOS Program
% define variables required for SOS program
syms x1 x2 v1 v2 u1;
vars = [x1; x2; v1; v2;u1];

% define lower and upper bounds
X_min = [-pi/2; -pi/2];
X_max = [pi/2; pi/2];
X_0_min = X_min;
X_0_max = X_max;
X_s_min = [-9*pi/18,-9*pi/18];
X_s_max = [-6*pi/18,-6*pi/18];
X_ns_min = X_s_max;
X_ns_max = X_max;
V_min = [-pi/2; -pi/2];
%V_max = [0.3; 0.3];
V_max = [pi/2; pi/2]; 
U_min = [-0.05; -0.05];
U_max = [0.05; 0.05]; 
% U1_min = [0.03; 0.03];


% control region
U1_all = (u1-U_min(1))*(U_max(1)-u1);

% all region
X1_all = (x1-X_min(1))*(X_max(1)-x1);
X2_all = (x2-X_min(2))*(X_max(2)-x2);
X_all  = [X1_all; X2_all];    
V1_all = (v1-V_min(1))*(V_max(1)-v1);
V2_all = (v2-V_min(2))*(V_max(2)-v2); 
V_all  = [V1_all; V2_all];

% initial region
% The polynomial functions for defining the semialgebraic region R_0(X_initial here);
g_01 = (x1-X_s_min(1))*(X_s_max(1)-x1); 
g_02 = (x2-X_ns_min(2))*(X_ns_max(2)-x2);
g_03 = -(c*x1-c*x2)^2+delta^2;
g_04 = V1_all;
g_05 = V2_all;
g_0  = [g_01; g_02; g_03; g_04; g_05];

% unsafe region
% The polynomial functions for defining the semialgebraic region R_u(X_unsafe here);
g_u1 = (x1-X_min(1))*(X_max(1)-x1); 
g_u2 = (x2-X_min(2))*(X_max(2)-x2);
g_u3 = (c*x1-c*x2)^2-delta^2-0.01;
g_u4 = V1_all;
g_u5 = V2_all;
g_u  = [g_u1; g_u2; g_u3; g_u4; g_u5];


nr_time = 200;
nr_iter = 30;

x1_traj = NaN(nr_iter, nr_time);
x2_traj = NaN(nr_iter, nr_time);
v1_traj = NaN(nr_iter, nr_time);
v2_traj = NaN(nr_iter, nr_time);
u1_traj = NaN(nr_iter, nr_time);
u2_traj = NaN(nr_iter, nr_time);
% % bc = NaN(nr_iter, nr_time);
% % bc_diff = NaN(nr_iter, nr_time);


% show results
Barrier_function =  0.2354*v1^2 - 0.4709*v1*v2 + 0.005946*v1*x1 - 0.005947*v1*x2 + 4.051e-5*v1 + 0.2354*v2^2 
- 0.00595*v2*x1 + 0.005948*v2*x2 + 5.357e-5*v2 + 0.9239*x1^2 - 1.848*x1*x2 - 7.712e-5*x1 + 0.9239*x2^2 
- 0.000111*x2 + 0.07164;
% bc_fh = matlabFunction(Barrier_function, 'Vars', [x1,x2,v1,v2]);

for i_iter = 1: nr_iter
    % generate initial state randomly
    x1_0 = (X_s_max(1)-X_s_min(1)).*rand(1) + X_s_min(1);
%     x2_0 = x1_0 + 0.7;
    x2_0 = (X_ns_max(1)-X_ns_min(1)).*rand(1) + X_ns_min(1);
%     x2_0 = 0.9375*x1_0*x1_0*x1_0 - 0.75*x1_0*x1_0 + 0.6125 * x1_0 + 1;
    while (-(c*x1_0-c*x2_0)^2+(delta)^2 < 0)
        x1_0 = (X_s_max(1)-X_s_min(1)).*rand(1) + X_s_min(1);
        x2_0 = (X_ns_max(1)-X_ns_min(1)).*rand(1) + X_ns_min(1);
    end
%     
    v1_0 = 0;
    v2_0 = 0;

    x1_traj(i_iter, 1) = x1_0;
    x2_traj(i_iter, 1) = x2_0;
    v1_traj(i_iter, 1) = v1_0;
    v2_traj(i_iter, 1) = v2_0;
    

        
    % define dynamics x(k+1)=f(x(k),w(k))
    for i_time = 1: nr_time

        u1_t = (U_max(1)-U_min(1)).*rand(1) + U_min(1)
        x1_t = x1_traj(i_iter, i_time) + v1_traj(i_iter, i_time);
        v1_t = g * (x1_traj(i_iter, i_time) - x1_traj(i_iter, i_time)*x1_traj(i_iter, i_time)*x1_traj(i_iter, i_time)/6) + 1/u1_t + v1_traj(i_iter, i_time);
        

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
        if x1_t <= X_min(1)
            x1_t = X_min(1);
        end
        if v1_t <= V_min(1)
            v1_t = V_min(1);
        end
        
%         if u1_t >= 0.04
%         u2_t = ... 
% -1.78863251602674*relu(-1.15284513837517*x1_traj(i_iter, i_time) - 0.46921627620952*x2_traj(i_iter, i_time) - 0.387229466682093*v1_traj(i_iter, i_time) + 0.144694673034578*v2_traj(i_iter, i_time) - 0.549046894192871*u1_t + 0.00255335722163473)...
% - 0.367777714413742*relu(-1.15104999047042*x1_traj(i_iter, i_time) - 1.09675476155998*x2_traj(i_iter, i_time) + 1.42221567981911*v1_traj(i_iter, i_time) - 0.206599689443102*v2_traj(i_iter, i_time)- 1.25805132784115*u1_t - 0.0897303833650123) ...
% - 0.00266333197556452*relu(-0.887043099299839*x1_traj(i_iter, i_time) - 0.0157554540093694*x2_traj(i_iter, i_time) - 0.642512367393646*v1_traj(i_iter, i_time) - 0.429830602483124*v2_traj(i_iter, i_time) + 0.395337173670947*u1_t + 0.425377037707252)...
% - 0.397523245137382*relu(-0.469038268140349*x1_traj(i_iter, i_time) + 0.0245119347410819*x2_traj(i_iter, i_time) - 0.0892561527923562*v1_traj(i_iter, i_time) - 1.12862708823075*v2_traj(i_iter, i_time) - 0.387255371609413*u1_t - 0.19081549023553) ...
% - 1.48189702008959*relu(-0.206071892377149*x1_traj(i_iter, i_time) - 1.09130422658573*x2_traj(i_iter, i_time) - 0.866278419207306*v1_traj(i_iter, i_time) + 0.153907672110862*v2_traj(i_iter, i_time) - 1.29357357596357*u1_t - 0.310436043086761)...
% + 0.000266989528356403*relu(-0.151715694476352*x1_traj(i_iter, i_time) - 0.185645010751303*x2_traj(i_iter, i_time) + 0.379998696472709*v1_traj(i_iter, i_time) - 0.853847226108817*v2_traj(i_iter, i_time) - 0.301139142882316*u1_t+ 0.576494268891921)...
% - 0.0019311050629382*relu(-0.0401909064784881*x1_traj(i_iter, i_time) - 0.292851816059341*x2_traj(i_iter, i_time) + 0.279459051472717*v1_traj(i_iter, i_time) + 0.970740307652485*v2_traj(i_iter, i_time) + 0.431027504209026*u1_t + 0.359369712315945)...
% + 0.00912707369025419*relu(0.0348048573594627*x1_traj(i_iter, i_time) + 0.0096845201617535*x2_traj(i_iter, i_time) + 0.499371404686363*v1_traj(i_iter, i_time) - 2.32620201135206*v2_traj(i_iter, i_time) - 1.01053152001986*u1_t - 0.314834239744889)...
% + 0.0486203738733524;
%         end
%         
%         if u1_t < 0.04
%             u2_t = u1_t - 0.001;
%         end
          u2_t = u1_t+0.938599427256428*x1_traj(i_iter, i_time) - 0.471195374919203*v1_traj(i_iter, i_time)-0.938599427256428*x1_traj(i_iter, i_time) + 0.471195374919203*v1_traj(i_iter, i_time);
%         u2_t =   0.8*x1_traj(i_iter, i_time)-0.8*x2_traj(i_iter, i_time)+1.5*v1_traj(i_iter, i_time)-1.5*v2_traj(i_iter, i_time)+u1_t;
    
        if u2_t  >= U_max(1)
            u2_t = U_max(1);
        end
        if u2_t  <= U_min(1)
            u2_t = U_min(1);
        end
%         
        x2_t = x2_traj(i_iter, i_time) + v2_traj(i_iter, i_time);
        v2_t = g * (x2_traj(i_iter, i_time) - x2_traj(i_iter, i_time)*x2_traj(i_iter, i_time)*x2_traj(i_iter, i_time)/6) + 1/u2_t + v2_traj(i_iter, i_time);
        
        if x2_t >= X_max(1)
            x2_t = X_max(1);
        end
        if v2_t >= V_max(1)
            v2_t = V_max(1);
        end
        if x2_t <= X_min(1)
            x2_t = X_min(1);
        end
        if v2_t <= V_min(1)
            v2_t = V_min(1);
        end              
%         bc(i_iter, i_time+1) = bc_fh(x1_t,x2_t,v1_t,v2_t);
%         bc_diff(i_iter, i_time)= bc(i_iter, i_time+1)-bc(i_iter, i_time);
        % dS1 & dS2
        x1_traj(i_iter, i_time+1) = x1_t;
        x2_traj(i_iter, i_time+1) = x2_t;
        v1_traj(i_iter, i_time+1) = v1_t;
        v2_traj(i_iter, i_time+1) = v2_t;
        u1_traj(i_iter, i_time) = u1_t;
        u2_traj(i_iter, i_time) = u2_t;        
    end
 end

%%
figure(1)
set(gcf, 'Position', [200, 200, 355, 350]);
my_color = get(gca, 'colororder');
nr_color = size(my_color, 1);
hold on; grid on; box on;

fill([0 9 0],[1 10 10],'c','facealpha',0.2,'edgealpha',0);
fill([1 10 10],[0 9 0],'c','facealpha',0.2,'edgealpha',0);
% fill([0.1 0.7 0.7 0.1 0.1],[0.7 0.7 1.35 0.75 0.7],'r','facealpha',0.2,'edgealpha',0);
% fill([0 1 1 0],[1 1 2 1],'r','facealpha',0.2,'edgealpha',0);
for i_iter = 1: nr_iter
    plot(x1_traj(i_iter, 1), x2_traj(i_iter, 1), '*', 'color', my_color(mod(i_iter, nr_color)+1, :));
  %    plot(x1_traj(i_iter, :), x2_traj(i_iter, :), 'color', my_color(mod(i_iter, nr_color)+1, :), 'LineWidth',2,'marker', 'o','MarkerSize',2);
  plot(x1_traj(i_iter, :), x2_traj(i_iter, :), 'color', my_color(mod(i_iter, nr_color)+1, :), 'LineWidth',1.5);
end
% plot([X_s_min(1) X_s_max(1)],[X_ns_min(2) X_s_max(1)], 'LineWidth',2, 'color', my_color(5, :));
% plot([X_s_max(1) X_s_max(1)],[X_s_max(1) (c*X_ns_min(1)+delta)/c], 'LineWidth',2, 'color', my_color(5, :));
% plot([X_s_min(1) X_s_max(1)],[X_ns_min(2) (c*X_ns_min(1)+delta)/c], 'LineWidth',2, 'color', my_color(5, :));
plot([0 1 1 0],[1 1 2 1], 'LineWidth',1, 'color','k');
% plot([X_s_min(1) X_s_max(1)],[X_ns_min(2) X_s_max(1)], 'LineWidth',1.5, 'color','k');
% plot([X_s_max(1) X_s_max(1)],[X_s_max(1) (c*X_ns_min(1)+delta)/c], 'LineWidth',1.5, 'color', 'k');
% plot([X_s_min(1) X_s_max(1)],[X_ns_min(2) (c*X_ns_min(1)+delta)/c], 'LineWidth',1.5, 'color', 'k');
axis([X_min(1) X_max(1) X_min(1) X_max(1)]);
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
fill([0 0.7 0.7 0],[0.8 1.5 1.7 1.7],'y','facealpha',0.2,'edgealpha',0);
fill([0 0.7 0.7 0 0],[0 0 0.7 0.7 0],'y','facealpha',0.2,'edgealpha',0);
fill([0 0.7 0.7 0 0],[0.7 0.7 1.5 0.8 0.7],'r','facealpha',0.2,'edgealpha',0);
plot([0 0.7 0.7 0 0],[0.7 0.7 1.5 0.8 0.7], 'LineWidth',1, 'color','r');
plot([0 0.7 0.7 0 0],[0.7 0.7 1.7 0.8 0.7], 'LineWidth',1, 'color','g');
axis([0 0.7 0 1.7]);
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










