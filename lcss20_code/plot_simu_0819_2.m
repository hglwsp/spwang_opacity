figure('color', 'w');
set(gcf, 'Position', [400, 400, 355, 350]);
my_color = get(gca, 'colororder');
nr_color = size(my_color, 1);
hold on; grid on; box on;

fill([10 29 10],[11 30 30],'c','facealpha',0.2,'edgealpha',0);
fill([11 30 30],[10 29 10],'c','facealpha',0.2,'edgealpha',0);
for i_iter = 1: nr_iter
  plot(x12_traj(i_iter, 1), x22_traj(i_iter, 1), '*', 'color', my_color(mod(i_iter, nr_color)+1, :));
  %    plot(x1_traj(i_iter, :), x2_traj(i_iter, :), 'color', my_color(mod(i_iter, nr_color)+1, :), 'LineWidth',2,'marker', 'o','MarkerSize',2);
  plot(x12_traj(i_iter, :), x22_traj(i_iter, :), 'color', my_color(mod(i_iter, nr_color)+1, :), 'LineWidth',1.5);
end

plot([21 22 22 21 21],[21 21 22 22 21], 'LineWidth',1.5, 'color','k');

axis([X_min(1) X_max(1) X_min(1) X_max(1)]);
axis square;
set(gca,'DataAspectRatio',[1 1 1]);
set(gca, 'Fontname', 'Times New Roman', 'FontSize', 11);
xlabel('$T_2$', 'Interpreter', 'latex', 'FontSize',12);
ylabel('$\hat T_2$', 'Interpreter', 'latex', 'FontSize',12);

% legend(my_legend, 'Location', 'SE', 'Interpreter', 'latex', 'FontSize',11)
FcnRemoveWhiteSpace(gcf,gca);

% enlarged details
axes('Position', [0.3,0.70,0.2,0.2]);
hold on; grid on; box on;
for i_iter = 1: nr_iter
    plot(x12_traj(i_iter, 1), x22_traj(i_iter, 1), '*', 'color', my_color(mod(i_iter, nr_color)+1, :));
  %  plot(x1_traj(i_iter, :), x2_traj(i_iter, :), 'color', my_color(mod(i_iter, nr_color)+1, :), 'LineWidth',2,'marker', 'o','MarkerSize',2);
     plot(x12_traj(i_iter, :), x22_traj(i_iter, :), 'color', my_color(mod(i_iter, nr_color)+1, :), 'LineWidth',1);
end
fill([10 29 10],[11 30 30],'c','facealpha',0.2,'edgealpha',0);
fill([11 30 30],[10 29 10],'c','facealpha',0.2,'edgealpha',0);
plot([21 22 22 21 21],[21 21 22 22 21], 'LineWidth',1.5, 'color','k');
axis([21 22.5 20.5 22]);


% enlarged details
% axes('Position', [0.7,0.3,0.2,0.2]);
% hold on; grid on; box on;
% for i_iter = 1: nr_iter
%     plot(x12_traj(i_iter, 1), x22_traj(i_iter, 1), '*', 'color', my_color(mod(i_iter, nr_color)+1, :));
%   %  plot(x1_traj(i_iter, :), x2_traj(i_iter, :), 'color', my_color(mod(i_iter, nr_color)+1, :), 'LineWidth',2,'marker', 'o','MarkerSize',2);
%      plot(x12_traj(i_iter, :), x22_traj(i_iter, :), 'color', my_color(mod(i_iter, nr_color)+1, :), 'LineWidth',1);
% end
% fill([0 49 0],[1 50 50],'r','facealpha',0.2,'edgealpha',0);
% fill([1 50 50],[0 49 0],'r','facealpha',0.2,'edgealpha',0);
% plot([21.5 22 22 21.5 21.5],[21 21 21.5 21.5 21], 'LineWidth',1, 'color','k');
% axis([1.7 5 2.7 6]);


% enlarged details change
axes('Position', [0.7,0.3,0.2,0.2]);
hold on; grid on; box on;
for i_iter = 1: nr_iter
    plot(x12_traj(i_iter, 1), x22_traj(i_iter, 1), '*', 'color', my_color(mod(i_iter, nr_color)+1, :));
  %  plot(x1_traj(i_iter, :), x2_traj(i_iter, :), 'color', my_color(mod(i_iter, nr_color)+1, :), 'LineWidth',2,'marker', 'o','MarkerSize',2);
     plot(x12_traj(i_iter, :), x22_traj(i_iter, :), 'color', my_color(mod(i_iter, nr_color)+1, :), 'LineWidth',1);
end
fill([10 29 10],[11 30 30],'c','facealpha',0.2,'edgealpha',0);
fill([11 30 30],[10 29 10],'c','facealpha',0.2,'edgealpha',0);
plot([21 22 22 21 21],[21 21 22 22 21], 'LineWidth',1.5, 'color','k');
axis([10 14 10 12]);

%printpdf(gcf, 'ex2_200819');


    