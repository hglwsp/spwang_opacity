function printpdf(gcf,figureName)
% example
% figure;
% x = -pi:0.01:pi;
% plot(x, sin(x));
% 
% xlabel('x');
% ylabel('sin(x)');
% grid on
% figName = 'examplefigpdf';
% printpdf(gcf,figName)

% resize the paper size
set(gcf,'Units','inches');
screenposition = get(gcf,'Position');
set(gcf,...
    'PaperPosition',[0 0 screenposition(3:4)],...
    'PaperSize',[screenposition(3:4)]);

% print
print('-painters','-dpdf','-r300', figureName)
end