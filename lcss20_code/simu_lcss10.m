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
delta = 0.8;
epsilon_1 =1;
epsilon_2 =1.001;  % epsilon_2 >= epsilon_1
kappa = 1 ;     % constant kappa in the last condition

%% SOS Program
% define variables required for SOS program
syms x1 x2 v1 v2 u1;
vars = [x1; x2; v1; v2;u1];

% define lower and upper bounds
X_min = [1; 1];
X_max = [5; 5];
X_0_min = X_min;
X_0_max = X_max;
X_s_min = [1; 1];
X_s_max = [1.1; 1.1];
X_ns_min = X_s_max;
X_ns_max = [1.6;1.6];
V_min = [0;0];
V_max = [0.1; 0.1]; 
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
    x2_0 = -396.83*x1_0*x1_0*x1_0 + 1237.30*x1_0*x1_0 - 1281.84 * x1_0 + 442.57;
    while (-(c*x1_0-c*x2_0)^2+(delta )^2 < 0)
        x1_0 = (X_s_max(1)-X_s_min(1)).*rand(1) + X_s_min(1);
        x2_0 = -396.83*x1_0*x1_0*x1_0 + 1237.30*x1_0*x1_0 - 1281.84 * x1_0 + 442.57;
    end
%     
    v1_0 = (V_max(1)-V_min(1)).*rand(1) + V_min(1);
    v2_0 = (V_max(1)-V_min(1)).*rand(1) + V_min(1);;

    x1_traj(i_iter, 1) = x1_0;
    x2_traj(i_iter, 1) = x2_0;
    v1_traj(i_iter, 1) = v1_0;
    v2_traj(i_iter, 1) = v2_0;
    

        
    % define dynamics x(k+1)=f(x(k),w(k))
    for i_time = 1: nr_time

        u1_t = (U_max(1)-U_min(1)).*rand(1) + U_min(1)
        x1_t = x1_traj(i_iter, i_time) + v1_traj(i_iter, i_time) + u1_t;
        v1_t = (exp(v1_traj(i_iter, i_time)) - 1) + 1*u1_t;
        

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
-0.00194089918525801*relu(-3.04310205931842*x1_traj(i_iter, i_time) + 1.00574033180266*x2_traj(i_iter, i_time) + 1.48929969166533*v1_traj(i_iter, i_time) - 1.34791723946631*v2_traj(i_iter, i_time) + 1.65710140197568*u1_t - 0.672608163239276)...
+ 0.00242874247579905*relu(-2.05000400150441*x1_traj(i_iter, i_time) + 0.6632051680725*x2_traj(i_iter, i_time) - 0.523864914734914*v1_traj(i_iter, i_time) - 0.0525854828290688*v2_traj(i_iter, i_time) + 1.12244996286789*u1_t - 0.374939265060864) ...
+ 1.03238116218058*relu(-2.00202072834275*x1_traj(i_iter, i_time) - 0.452864191776889*x2_traj(i_iter, i_time) + 0.301301618883869*v1_traj(i_iter, i_time) + 0.55736388783268*v2_traj(i_iter, i_time) + 0.443794096770803*u1_t + 0.86314384243385)...
+ 0.64045876776299*relu(-0.787142411235495*x1_traj(i_iter, i_time) - 0.144241152759122*x2_traj(i_iter, i_time) - 0.143113695584753*v1_traj(i_iter, i_time) - 0.146631258696995*v2_traj(i_iter, i_time) + 0.280574468825913*u1_t + 0.555679264493473)...
- 0.966978581321368*relu(-0.606051349512228*x1_traj(i_iter, i_time) + 0.0788108348349424*x2_traj(i_iter, i_time) + 0.212837401213284*v1_traj(i_iter, i_time) - 1.52903228123965*v2_traj(i_iter, i_time) - 0.822875666199395*u1_t + 0.216853398089884)...
- 2.23933056598771*relu(-0.594264046039552*x1_traj(i_iter, i_time) + 0.146047764739396*x2_traj(i_iter, i_time) + 0.447894370805756*v1_traj(i_iter, i_time) + 0.442953660540369*v2_traj(i_iter, i_time) - 0.0694214285593614*u1_t - 0.503568048151583)...
- 0.00036754482974955*relu(-0.522320683056415*x1_traj(i_iter, i_time) - 1.0004025512413*x2_traj(i_iter, i_time) + 1.14463232986057*v1_traj(i_iter, i_time) + 1.82866127694179*v2_traj(i_iter, i_time) + 1.30055805975999*u1_t + 2.89921075313481) ...
+ 2.0647499465471*relu(0.150664864315063*x1_traj(i_iter, i_time) - 0.630805453534331*x2_traj(i_iter, i_time) + 0.309031855344938*v1_traj(i_iter, i_time) + 1.45921063034412*v2_traj(i_iter, i_time) - 0.839762775738244*u1_t - 0.523423810326477)...
+ 0.0482491116245389
    
        if u2_t  >= U_max(1)
            u2_t = U_max(1);
        end
        if u2_t  <= U_min(1)
            u2_t = U_min(1);
        end
%         
        x2_t = x2_traj(i_iter, i_time) + v2_traj(i_iter, i_time) + u2_t;
        v2_t = (exp(v2_traj(i_iter, i_time)) - 1 )+ 1*u2_t;
        
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

fill([1 4.2 1],[1.8 5 5],'c','facealpha',0.2,'edgealpha',0);
fill([1.8 5 5],[1 4.2 1],'c','facealpha',0.2,'edgealpha',0);
for i_iter = 1: nr_iter
    plot(x1_traj(i_iter, 1), x2_traj(i_iter, 1), '*', 'color', my_color(mod(i_iter, nr_color)+1, :));
  %    plot(x1_traj(i_iter, :), x2_traj(i_iter, :), 'color', my_color(mod(i_iter, nr_color)+1, :), 'LineWidth',2,'marker', 'o','MarkerSize',2);
  plot(x1_traj(i_iter, :), x2_traj(i_iter, :), 'color', my_color(mod(i_iter, nr_color)+1, :), 'LineWidth',1.5);
end
% plot([X_s_min(1) X_s_max(1)],[X_ns_min(2) X_s_max(1)], 'LineWidth',2, 'color', my_color(5, :));
% plot([X_s_max(1) X_s_max(1)],[X_s_max(1) (c*X_ns_min(1)+delta)/c], 'LineWidth',2, 'color', my_color(5, :));
% plot([X_s_min(1) X_s_max(1)],[X_ns_min(2) (c*X_ns_min(1)+delta)/c], 'LineWidth',2, 'color', my_color(5, :));
% fill([1 1.1 1.1 1 1],[1.1 1.1 1.6 1.5 1.1],'r','facealpha',0.2,'edgealpha',0);
plot([1 1.1 1.1 1 1],[1.1 1.1 1.9 1.8 1.1], 'LineWidth',1, 'color','k');
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
fill([1 1.1 1.1 1],[1.5 1.6 2.05 2.05],'y','facealpha',0.2,'edgealpha',0);
fill([1 1.1 1.1 1 1],[1 1 1.1 1.1 1],'y','facealpha',0.2,'edgealpha',0);
fill([1 1.1 1.1 1 1],[1.1 1.1 1.6 1.5 1.1],'r','facealpha',0.2,'edgealpha',0);
plot([1 1.1 1.1 1 1],[1.1 1.1 1.6 1.5 1.1], 'LineWidth',1, 'color','r');
plot([1 1.1 1.1 1 1],[1.1 1.1 2.05 1.95 1.1], 'LineWidth',1, 'color','g');
axis([1 2.05 1 2.05]);
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










