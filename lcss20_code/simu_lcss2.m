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
delta = 1.25;
epsilon_1 =1;
epsilon_2 =1.001;  % epsilon_2 >= epsilon_1
kappa = 1 ;     % constant kappa in the last condition

%% SOS Program
% define variables required for SOS program
syms x1 x2 v1 v2 u1;
vars = [x1; x2; v1; v2;u1];

% define lower and upper bounds
X_min = [2;2];
X_max = [12; 12];
X_0_min = X_min;
X_0_max = X_max;
X_s_min = [10; 10];
X_s_max = [11; 11];
X_ns_min = X_s_max;
X_ns_max = X_max;
V_min = [0;0];
V_max = [0.1; 0.1]; 
U_min = [-0.05;-0.05];
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


nr_time = 100;
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
Barrier_function =  0.2354*v1^2 - 0.4709*v1*v2 + 0.005946*v1*x1 - 0.005947*v1*x2 + 4.051e-5*v1 + 0.2354*v2^2 ...
- 0.00595*v2*x1 + 0.005948*v2*x2 + 5.357e-5*v2 + 0.9239*x1^2 - 1.848*x1*x2 - 7.712e-5*x1 + 0.9239*x2^2 ...
- 0.000111*x2 + 0.07164;
% bc_fh = matlabFunction(Barrier_function, 'Vars', [x1,x2,v1,v2]);

for i_iter = 1: nr_iter
    % generate initial state randomly
    x1_0 = (X_s_max(1)-X_s_min(1)).*rand(1) + X_s_min(1);
    x2_0 = (X_ns_max(1)-X_ns_min(1)).*rand(1) + X_ns_min(1);
    while (-(c*x1_0-c*x2_0)^2+delta^2 - 0.2 < 0)
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
    
%     bc(i_iter, 1) = bc_fh(x1_0,x2_0,v1_0,v2_0);
%     bc_diff(1)= 0;
        
    % define dynamics x(k+1)=f(x(k),w(k))
    for i_time = 1: nr_time
        % x1_t = -2*x1 + v1 + u
        % v1_t = 0.01*(x1 + 2*v1 + u)
        u1_t = (U_max(1)-U_min(1)).*rand(1) + U_min(1);
        x1_t = -2*x1_traj(i_iter, i_time) + v1_traj(i_iter, i_time) + u1_t;
        v1_t = 0.01*(x1_traj(i_iter, i_time) + 2*v1_traj(i_iter, i_time) + u1_t);
        

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
        u2_t = 0.00178211117461337*x1_traj(i_iter, i_time) + 0.000557651387936453*x2_traj(i_iter, i_time) + 0.172873548952826*v1_traj(i_iter, i_time) - 0.0128141896580516*v2_traj(i_iter, i_time) - 0.0896533243394356*u1_t;
%         u2_t = 0.8*x1_traj(i_iter, i_time)-0.8*x2_traj(i_iter, i_time)+1.5*v1_traj(i_iter, i_time)-1.5*v2_traj(i_iter, i_time)+u1_t;

        
        if u2_t  >= U_max(1)
            u2_t = U_max(1);
        end
        if u2_t  <= U_min(1)
            u2_t = U_min(1);
        end
        
        x2_t = -2*x2_traj(i_iter, i_time) + v2_traj(i_iter, i_time) + u2_t;
        v2_t = 0.01*(x2_traj(i_iter, i_time) + 2*v1_traj(i_iter, i_time) + u2_t);
        
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
figure('color', 'w');
set(gcf, 'Position', [200, 200, 355, 350]);
my_color = get(gca, 'colororder');
nr_color = size(my_color, 1);
hold on; grid on; box on;

fill([2 10.5 0],[3 12 12],'r','facealpha',0.2,'edgealpha',0);
fill([3 12 12],[2 10.5 0],'r','facealpha',0.2,'edgealpha',0);
for i_iter = 1: nr_iter
    plot(x1_traj(i_iter, 1), x2_traj(i_iter, 1), '*', 'color', my_color(mod(i_iter, nr_color)+1, :));
  %    plot(x1_traj(i_iter, :), x2_traj(i_iter, :), 'color', my_color(mod(i_iter, nr_color)+1, :), 'LineWidth',2,'marker', 'o','MarkerSize',2);
  plot(x1_traj(i_iter, :), x2_traj(i_iter, :), 'color', my_color(mod(i_iter, nr_color)+1, :), 'LineWidth',1.5);
end
% plot([X_s_min(1) X_s_max(1)],[X_ns_min(2) X_s_max(1)], 'LineWidth',2, 'color', my_color(5, :));
% plot([X_s_max(1) X_s_max(1)],[X_s_max(1) (c*X_ns_min(1)+delta)/c], 'LineWidth',2, 'color', my_color(5, :));
% plot([X_s_min(1) X_s_max(1)],[X_ns_min(2) (c*X_ns_min(1)+delta)/c], 'LineWidth',2, 'color', my_color(5, :));
plot([X_s_min(1) X_s_max(1)],[X_ns_min(2) X_s_max(1)], 'LineWidth',1.5, 'color','k');
plot([X_s_max(1) X_s_max(1)],[X_s_max(1) (c*X_ns_min(1)+delta)/c], 'LineWidth',1.5, 'color', 'k');
plot([X_s_min(1) X_s_max(1)],[X_ns_min(2) (c*X_ns_min(1)+delta)/c], 'LineWidth',1.5, 'color', 'k');
axis([X_min(1) X_max(1) X_min(1) X_max(1)]);
axis square;
set(gca,'DataAspectRatio',[1 1 1],'Fontname','Arial');
set(gca, 'FontSize', 11,'Fontname','Arial');
xlabel('$x_1$', 'Interpreter', 'latex', 'FontSize',12,'Fontname','Arial');
ylabel('$\hat x_1$', 'Interpreter', 'latex', 'FontSize',12,'Fontname','Arial');

% legend(my_legend, 'Location', 'SE', 'Interpreter', 'latex', 'FontSize',11)
FcnRemoveWhiteSpace(gcf,gca);

% enlarged details
axes('Position', [0.22,0.65,0.27,0.257]);
hold on; grid on; box on;
for i_iter = 1: nr_iter
    plot(x1_traj(i_iter, 1), x2_traj(i_iter, 1), '*', 'color', my_color(mod(i_iter, nr_color)+1, :));
  %  plot(x1_traj(i_iter, :), x2_traj(i_iter, :), 'color', my_color(mod(i_iter, nr_color)+1, :), 'LineWidth',2,'marker', 'o','MarkerSize',2);
     plot(x1_traj(i_iter, :), x2_traj(i_iter, :), 'color', my_color(mod(i_iter, nr_color)+1, :), 'LineWidth',1);
end
fill([2 10.5 0],[3 12 12],'r','facealpha',0.2,'edgealpha',0);
fill([3 12 12],[2 10.5 0],'r','facealpha',0.2,'edgealpha',0);
% plot([X_s_min(1) X_s_max(1)],[X_ns_min(2) X_s_max(1)], 'LineWidth',1.5, 'color', my_color(5, :));
% plot([X_s_max(1) X_s_max(1)],[X_s_max(1) (c*X_ns_min(1)+delta)/c], 'LineWidth',1.5, 'color', my_color(5, :));
% plot([X_s_min(1) X_s_max(1)],[X_ns_min(2) (c*X_ns_min(1)+delta)/c], 'LineWidth',1.5, 'color', my_color(5, :));
plot([X_s_min(1) X_s_max(1)],[X_ns_min(2) X_s_max(1)], 'LineWidth',1.5, 'color','k');
plot([X_s_max(1) X_s_max(1)],[X_s_max(1) (c*X_ns_min(1)+delta)/c], 'LineWidth',1.5, 'color', 'k');
plot([X_s_min(1) X_s_max(1)],[X_ns_min(2) (c*X_ns_min(1)+delta)/c], 'LineWidth',1.5, 'color', 'k');
axis([0 2 0.3 2.2]);
set(gca,'DataAspectRatio',[1 1 1],'Fontname','Arial');
set(gca, 'FontSize', 11,'Fontname','Arial');

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
% 
% xlswrite('D:\wsppythonProject\opacity_loss1u\plot_traj\data_x1.xlsx',x1_traj)
% xlswrite('D:\wsppythonProject\opacity_loss1u\plot_traj\data_x2.xlsx',x2_traj)
% 
% 
% xlswrite('D:\wsppythonProject\opacity_loss1u\plot_traj\data_v1.xlsx',v1_traj)
% xlswrite('D:\wsppythonProject\opacity_loss1u\plot_traj\data_v2.xlsx',v2_traj)








