%% ��άx-y-z����
%��ͬ��ʼ��������ݻ�ͼ
%%
%ͼ11������1
clc,clear; 
figure(11);
Rp=150,Cph=85,Cpl=0,Cp=10,Bt=40,Fp=40,Mp=20,Ct=10,Ft=20,Mt=15,Cg=15,Tg=40;  
for i=0.1:0.2:1
    for j=0.1:0.2:1
        for k=0.1:0.2:1   
        [t,y]=ode45(@(t,y) yaopin(t,y,Rp,Cph,Cpl,Cp,Bt,Fp,Mp,Ct,Ft,Mt,Cg,Tg),[0 50],[i j k]);               
        %plot3(y(:,1),y(:,2),y(:,3),'linewidth',1);
        plot3(y(:,1),y(:,2),y(:,3),'rp','linewidth',1); %����ɫ��Ϊ��ɫ�����͸�Ϊ����ǡ�
        set(gca,'XTick',[0:0.2:1],'YTick',[0:0.2:1],'ZTick',[0:0.2:1])
        hold on
        axis([0 1 0 1 0 1])
        view([45 10])
        end
    end
end
grid on
hold on
xlabel('x','Rotation',0);
ylabel('y','Rotation',0);
zlabel('z','Rotation',360,'position',[0 0 1.05]);
title('ͼ  11 ����1�ݻ�50�ν��','FontWeight','bold','position',[1 0 -0.13]);
%%
%ͼ12������2
clc,clear; 
figure(12);
Rp=150,Cph=105,Cpl=0,Cp=10,Bt=50,Fp=25,Mp=15,Ct=10,Ft=18,Mt=12,Cg=15,Tg=40;  
for i=0.1:0.2:1
    for j=0.1:0.2:1
        for k=0.1:0.2:1   
        [t,y]=ode45(@(t,y) yaopin(t,y,Rp,Cph,Cpl,Cp,Bt,Fp,Mp,Ct,Ft,Mt,Cg,Tg),[0 50],[i j k]);               
        plot3(y(:,1),y(:,2),y(:,3),'linewidth',1);
        set(gca,'XTick',[0:0.2:1],'YTick',[0:0.2:1],'ZTick',[0:0.2:1])
        hold on
        axis([0 1 0 1 0 1])
        view([45 10])
        end
    end
end
grid on
hold on
xlabel('x','Rotation',0);
ylabel('y','Rotation',0);
zlabel('z','Rotation',360,'position',[0 0 1.05]);
title('ͼ  12 ����2�ݻ�50�ν��','FontWeight','bold','position',[1 0 -0.13]);