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
delta = 1.2;
epsilon_1 =1;
epsilon_2 =1.001;  % epsilon_2 >= epsilon_1
kappa = 1 ;     % constant kappa in the last condition
pi = 3.1415
%% SOS Program
% define variables required for SOS program
syms x1 x2 v1 v2 u1;
vars = [x1; x2; v1; v2;u1];

% define lower and upper bounds
X_min = [0; 0];
X_max = [1.6; 1.6];
X_0_min = X_min;
X_0_max = X_max;
X_s_min = [0; 0];
X_s_max = [0.1; 0.1];
X_ns_min = X_s_max;
X_ns_max = [0.7;0.7];
V_min = [0;0];
V_max = [1.6; 1.6]; 
U_min = [-0.01; -0.01];
U_max = [0.01; 0.01]; 



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
    x2_0 = (X_ns_max(1)-X_ns_min(1)).*rand(1) + X_ns_min(1);
    while (-(c*x1_0-c*x2_0)^2+(delta - 0.6)^2 < 0)
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
        x1_t = 0.1*x1_traj(i_iter, i_time) + u1_t;
        v1_t = sin(2*pi*x1_traj(i_iter, i_time)) + 1;
        

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

        u2_t =...
0.361704074955294*relu(-0.62618907075351*x1_traj(i_iter, i_time) - 0.114589536910878*x2_traj(i_iter, i_time) - 0.572188532531005*v1_traj(i_iter, i_time) - 0.0890064364884792*v2_traj(i_iter, i_time) - 0.8758778853924*u1_t + 0.0162770452948237)...
+ 0.904846948283075*relu(-0.588002346478988*x1_traj(i_iter, i_time) - 1.12660978021541*x2_traj(i_iter, i_time) - 0.154122582479284*v1_traj(i_iter, i_time) - 0.551898704543572*v2_traj(i_iter, i_time) + 0.312964316607039*u1_t + 0.0100151544455703)...
- 0.0009024703163863*relu(-0.545114947258825*x1_traj(i_iter, i_time) - 1.58347892939085*x2_traj(i_iter, i_time) + 1.0917401146381*v1_traj(i_iter, i_time) + 0.561747202874108*v2_traj(i_iter, i_time) - 1.14571928153371*u1_t - 0.297260540163364)...
+ 2.54634472679982*relu(-0.331687984200601*x1_traj(i_iter, i_time) + 0.554552412555428*x2_traj(i_iter, i_time) + 0.00731898503380615*v1_traj(i_iter, i_time) - 0.481095489506566*v2_traj(i_iter, i_time) + 0.740089997283516*u1_t - 0.903479628484817)...
- 0.00104409854207344*relu(-0.287670943197966*x1_traj(i_iter, i_time) + 0.363521914626095*x2_traj(i_iter, i_time) + 0.401829986393158*v1_traj(i_iter, i_time) - 1.03843708718742*v2_traj(i_iter, i_time) + 0.644363666215601*u1_t + 0.223570380735473)...
- 0.719179788159233*relu(-0.0760256855135403*x1_traj(i_iter, i_time) - 0.223389380764645*x2_traj(i_iter, i_time) + 0.41476336927782*v1_traj(i_iter, i_time) + 0.868867793901723*v2_traj(i_iter, i_time) + 0.194493857738091*u1_t - 2.05553073306286)...
+ 1.38121646152658*relu(0.0169047498873838*x1_traj(i_iter, i_time) + 0.242738430089944*x2_traj(i_iter, i_time) - 0.604491691558423*v1_traj(i_iter, i_time) - 0.774525897133782*v2_traj(i_iter, i_time) + 0.251871454768934*u1_t- 0.421416046497285)...
+ 1.30143250243975*relu(0.0312720569849066*x1_traj(i_iter, i_time) - 0.906012474123742*x2_traj(i_iter, i_time) - 0.357666330374043*v1_traj(i_iter, i_time) + 0.885551810939743*v2_traj(i_iter, i_time) + 0.628176616880495*u1_t - 1.47374683297574) ...
- 0.00588274956024331
    
        if u2_t  >= U_max(1)
            u2_t = U_max(1);
        end
        if u2_t  <= U_min(1)
            u2_t = U_min(1);
        end
%         
        x2_t = 0.1*x2_traj(i_iter, i_time) + u2_t;
        v2_t = sin(2*pi*x2_traj(i_iter, i_time)) + 1;
        
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

fill([0 0.4 0],[1.2 1.6 1.6],'c','facealpha',0.2,'edgealpha',0);
fill([1.2 1.6 1.6],[0 0.4 0],'c','facealpha',0.2,'edgealpha',0);
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
figure(2)
set(gcf, 'Position', [400, 400, 355, 350]);
my_color = get(gca, 'colororder');
nr_color = size(my_color, 1);
hold on; grid on; box on;
for i_iter = 1: nr_iter
     plot(x1_traj(i_iter, 1), x2_traj(i_iter, 1), '*', 'color', my_color(mod(i_iter, nr_color)+1, :));  %  plot(x1_traj(i_iter, :), x2_traj(i_iter, :), 'color', my_color(mod(i_iter, nr_color)+1, :), 'LineWidth',2,'marker', 'o','MarkerSize',2);
%      plot(x12_traj(i_iter, :), x22_traj(i_iter, :), 'color', my_color(mod(i_iter, nr_color)+1, :), 'LineWidth',1);
end
fill([0 0.1 0.1 0],[0.6 0.7 1.3 1.3],'c','facealpha',0.2,'edgealpha',0);
plot([0 0.1 0.1 0],[0.1 0.1 1.3 0.1], 'LineWidth',1, 'color','k');
axis([0 0.1 0 1.3]);
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










