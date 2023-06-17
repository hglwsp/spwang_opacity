%% load the stored data
%load('deg6_max_0819.mat')
%bc_fh = matlabFunction(Barrier_function, 'Vars', [x11,x12,x21,x22]); 

%%
nr_time = 300;
nr_iter = 30;

x11_traj = NaN(nr_iter, nr_time);
x12_traj = NaN(nr_iter, nr_time);
x21_traj = NaN(nr_iter, nr_time);
x22_traj = NaN(nr_iter, nr_time);

u11_traj = NaN(nr_iter, nr_time);
u12_traj = NaN(nr_iter, nr_time);
u21_traj = NaN(nr_iter, nr_time);
u22_traj = NaN(nr_iter, nr_time);

x12_0 = 21.75;
x22_0 = 21.25;
x11_0 = 21.5;
x21_0 = 21.5;

X_min = 10;
X_max = 30;
U_min=0;   
U_max=1; 

%% Parameters
alpha = 0.05;
Te=15;
ah=3.6e-3;
Th=55;
ae=0.008;

delta=1;
epsilon_1=0;
epsilon_2=0.001;
kappa = 1 ;     % constant kappa in the last condition


% bc = NaN(nr_iter, nr_time);
% bc_diff = NaN(nr_iter, nr_time);

%%
for i_iter = 1: nr_iter
    

    x11_00 = (22-21.5).*rand(1) + 21.5;
    x21_00 = (21.5-21).*rand(1) + 21;

    
    x12_00 = (22-21).*rand(1) + 21;
    x22_00 = (22-21).*rand(1) + 21;
%     while (0.5-(x11_00-x11_0)^2-(x21_00-x21_0)^2 < 0)
%         x12_00 = (22-21).*rand(1) + 21;
%         x21_00 = (22-21).*rand(1) + 21;
%     end
        
    x11_traj(i_iter, 1) = x11_00;
    x12_traj(i_iter, 1) = x12_00;
    x21_traj(i_iter, 1) = x21_00;
    x22_traj(i_iter, 1) = x22_00;
    
%     bc(i_iter, 1) = bc_fh(x11_0,x12_00,x21_0,x22_00);
%     bc_diff(1)= 0;
    
    
    
    x11_t = x11_00;
    x12_t = x12_00;
    x21_t = x21_00;
    x22_t = x22_00;
    

 for i_time = 1: nr_time
     
% 调整，争取 10 - 30
%         u11_t = U_min;
%         u12_t = U_min;
% 
%         u11_t = 1;
%         u12_t = 1;
%         
        % consider u as a function with x
%chatGPT  
%           u11_t=(x11_traj(i_iter, i_time)-10)/20;
%           u12_t=(x12_traj(i_iter, i_time)-10)/20;
%chatGPT 2
        a=1;
        b=1;
        u11_t = (x11_traj(i_iter, i_time)-10)*(30-x11_traj(i_iter, i_time))*(x11_traj(i_iter, i_time)-a)/(400 + b*(x11_traj(i_iter, i_time)-a)^2);
        u12_t = (x12_traj(i_iter, i_time)-10)*(30-x12_traj(i_iter, i_time))*(x12_traj(i_iter, i_time)-a)/(400 + b*(x12_traj(i_iter, i_time)-a)^2);
%         u11_t = 0.001*(593.32455521463 - 4.41108962128645*x11_traj(i_iter, i_time));
%         u12_t = 0.001*(593.32455521463 - 4.41108962128645*x12_traj(i_iter, i_time));
        
        x11_t = (1-2*alpha-ae-ah*u11_t)*x11_traj(i_iter, i_time)+ alpha*x12_traj(i_iter, i_time)+ ae*Te + ah*Th*u11_t;
        x12_t = (1-2*alpha-ae-ah*u12_t)*x12_traj(i_iter, i_time)+ alpha*x11_traj(i_iter, i_time)+ ae*Te + ah*Th*u12_t;
        
               
        if x11_t >= 30
            x11_t = 30;
        end
        if x11_t <= 10
            x11_t = 10;
        end
        if x12_t >= 30
            x12_t = 30;
        end
        if x12_t <= 10
            x12_t = 10;
        end
        
%         u21_t = (U_max-U_min).*rand(1) + U_min;
%         u22_t = (U_max-U_min).*rand(1) + U_min;

%           u21_t=(x11_traj(i_iter, i_time)-10)/20;
%           u22_t=(x12_traj(i_iter, i_time)-10)/20;

        u21_t = (x21_traj(i_iter, i_time)-10)*(30-x21_traj(i_iter, i_time))*(x21_traj(i_iter, i_time)-a)/(400 + b*(x21_traj(i_iter, i_time)-a)^2);
        u22_t = (x22_traj(i_iter, i_time)-10)*(30-x22_traj(i_iter, i_time))*(x22_traj(i_iter, i_time)-a)/(400 + b*(x22_traj(i_iter, i_time)-a)^2);

%         u21_t = 0.001*(593.32455521463 - 4.41108962128645*x21_traj(i_iter, i_time));
%         u22_t = 0.001*(593.32455521463 - 4.41108962128645*x22_traj(i_iter, i_time));
%         
        
        
        x21_t = (1-2*alpha-ae-ah*u21_t)*x21_traj(i_iter, i_time)+ alpha*x22_traj(i_iter, i_time)+ ae*Te + ah*Th*u21_t;
        x22_t = (1-2*alpha-ae-ah*u22_t)*x22_traj(i_iter, i_time)+ alpha*x21_traj(i_iter, i_time)+ ae*Te + ah*Th*u22_t;
        
        if x21_t >= 30
            x21_t = 30;
        end
        if x21_t <= 10
            x21_t = 10;
        end
        if x22_t >= 30
            x22_t =30;
        end
        if x22_t <= 10
            x22_t = 10;
        end
        
        %
%         bc(i_iter, i_time+1)= bc_fh(x11_t,x12_t,x21_t,x22_t);
%         bc_diff(i_iter, i_time)= bc(i_iter, i_time+1)-bc(i_iter, i_time);
        
        x12_traj(i_iter, i_time+1)  = x12_t;
        x22_traj(i_iter, i_time+1)  = x22_t;
        x11_traj(i_iter, i_time+1)  = x11_t;
        x21_traj(i_iter, i_time+1)  = x21_t;
        
        u11_traj(i_iter, i_time)  = u11_t;
        u12_traj(i_iter, i_time)  = u12_t;
        u21_traj(i_iter, i_time)  = u21_t;
        u22_traj(i_iter, i_time)  = u22_t;
    end
end
    %% plot
%%
plot_simu_0819_2; 
xlswrite('D:\pythonProject\lcss\lcss\ecc_1\plot_traj\data_u11.xlsx',u11_traj);
xlswrite('D:\pythonProject\lcss\lcss\ecc_1\plot_traj\data_u12.xlsx',u12_traj);
xlswrite('D:\pythonProject\lcss\lcss\ecc_1\plot_traj\data_u21.xlsx',u21_traj);
xlswrite('D:\pythonProject\lcss\lcss\ecc_1\plot_traj\data_u22.xlsx',u22_traj);

