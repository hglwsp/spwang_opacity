...



nr_time = 300;
nr_iter = 35;

x1_traj = NaN(nr_iter, nr_time);
x2_traj = NaN(nr_iter, nr_time);
v1_traj = NaN(nr_iter, nr_time);
v2_traj = NaN(nr_iter, nr_time);
u1_traj = NaN(nr_iter, nr_time);
u2_traj = NaN(nr_iter, nr_time);
bc = NaN(nr_iter, nr_time);
bc_diff = NaN(nr_iter, nr_time);

for i_iter = 1: nr_iter
    % generate initial state randomly
    x1_0 = (X_s_max(1)-X_s_min(1)).*rand(1) + X_s_min(1);
    x2_0 = (X_ns_max(1)-X_ns_min(1)).*rand(1) + X_ns_min(1);
    while (-(c*x1_0-c*x2_0)^2+delta^2 < 0)
        x1_0 = (X_s_max(1)-X_s_min(1)).*rand(1) + X_s_min(1);
        x2_0 = (X_ns_max(1)-X_ns_min(1)).*rand(1) + X_ns_min(1);
    end
    
    v1_0 = 0;
    v2_0 = 0;
    % v1_0 = (V_max(1)-V_min(1)).*rand(1) + V_min(1);
    % v2_0 = (V_max(1)-V_min(1)).*rand(1) + V_min(1);
    
    x1_traj(i_iter, 1) = x1_0;
    x2_traj(i_iter, 1) = x2_0;
    v1_traj(i_iter, 1) = v1_0;
    v2_traj(i_iter, 1) = v2_0;
    
    bc(i_iter, 1) = bc_fh(x1_0,x2_0,v1_0,v2_0);
    %bc(1) = (x1_0-x2_0)^2;
    %bc(1)=  0.8957*x1_0^2 - 1.791*x1_0*x2_0  + 0.8957*x2_0^2 + 0.1014;
    bc_diff(1)= 0;
        
    % define dynamics x(k+1)=f(x(k),w(k))
    for i_time = 1: nr_time
        u1_t = (U_max(1)-U_min(1)).*rand(1) + U_min(1);
        x1_t = x1_traj(i_iter, i_time) + v1_traj(i_iter, i_time) + 0.5*u1_t;
        v1_t = v1_traj(i_iter, i_time) + 1*u1_t;
        
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
        
        u2_t = 0.8*x1_traj(i_iter, i_time)-0.8*x2_traj(i_iter, i_time)+1.5*v1_traj(i_iter, i_time)-1.5*v2_traj(i_iter, i_time)+u1_t;
        
        if u2_t  >= U_max(1)
            u2_t = U_max(1);
        end
        if u2_t  <= U_min(1)
            u2_t = U_min(1);
        end
        
        x2_t = x2_traj(i_iter, i_time) + v2_traj(i_iter, i_time) + 0.5*u2_t;
        v2_t = v2_traj(i_iter, i_time) + 1*u2_t;
        
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
               
        bc(i_iter, i_time+1) = bc_fh(x1_t,x2_t,v1_t,v2_t);
        % bc(i+1)=(x1_t-x2_t)^2;
        % bc(i+1)=  0.8957*x1_t^2 - 1.7914*x1_t*x2_t  + 0.8957*x2_t^2 + 0.1043;
        bc_diff(i_iter, i_time)= bc(i_iter, i_time+1)-bc(i_iter, i_time);
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

fill([0 9 0],[1 10 10],'r','facealpha',0.2,'edgealpha',0);
fill([1 10 10],[0 9 0],'r','facealpha',0.2,'edgealpha',0);
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
fill([0 9 0],[1 10 10],'r','facealpha',0.2,'edgealpha',0);
fill([1 10 10],[0 9 0],'r','facealpha',0.2,'edgealpha',0);
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

% figure(4);
% hold on;
% for i_iter = 1:2
%     plot([1:nr_time],u1_traj(i_iter, :),'color', my_color(5, :), 'LineWidth',1);
%     plot([1:nr_time],u2_traj(i_iter, :),'color', my_color(3, :), 'LineWidth',1);
% end
% plot([1:nr_time],0.05*ones(nr_time),'LineStyle', '--','color', my_color(2, :), 'LineWidth',1);
% plot([1:nr_time],-0.05*ones(nr_time),'LineStyle','--','color', my_color(2, :), 'LineWidth',1);
% axis([0 nr_time -0.08 0.08]);



% figure(5);
% hold on;
% for i_iter = 1:50
%     plot([1:nr_time],bc(i_iter, 1:nr_time),'color', my_color(5, :), 'LineWidth',1);
%     plot([1:nr_time],bc_diff(i_iter, :),'color', my_color(3, :), 'LineWidth',1);
% end
% 
% max(bc_diff)
% find(bc_diff==max(bc_diff))




