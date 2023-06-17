clc; clear; close all;
% Main code for 2-d room temperature for opacity
% Main code for lcss20 example2
echo on;
%% Parameters
alpha = 0.05;
ae=8e-3;
Te=15;
ah=3.6e-3;
Th=55;
ae=0.008;

delta=3;
epsilon_1=0;
epsilon_2=0.001;
kappa = 1 ;     % constant kappa in the last condition

%% SOS Program
% define variables required for SOS program
syms x11 x12 x21 x22 u2;
vars = [x11; x12; x21; x22; u2];

% define lower and upper bounds
X_min = 10;
X_max = 30;


U_min=0;   
U_max=1; 
U2_all = (u2-U_min)*(U_max-u2);

%% initial region
% 
% x12_0 = 22;
% x22_0 = 21.01;
% x11_0 = 23;
% x21_0 = 20;
x12_0 = 21.75;
x22_0 = 21.25;
x11_0 = 21.5;
x21_0 = 21.5;
g_01 = 2*0.25^2-(x12-x12_0)^2-(x22-x22_0)^2;
g_02 = 0.5-(x11-x11_0)^2-(x21-x21_0)^2;
g_0 = [g_01;g_02];

%% boundary
% g_b1 = (x11-0)*(50-x11);
% g_b2 = (x21-0)*(50-x21);
g_b1 = 35.4^2-(x11-25)^2-(x21-25)^2;
g_b3 = delta^2-(x12-50)^2-(x22-50)^2;
g_b4 = delta^2-x12^2-x22^2;

%% closure
%g_u1 =  35.4^2-(x12-25)^2-(x22-25)^2;
g_u3 = -(x12-x22)^2+delta^2;
g_u4 = 35.4^2-(x11-25)^2-(x21-25)^2;
g_u=[g_u3;g_u4];

%% initialize the sum of squares program
prog = sosprogram(vars);

% define monomials
degree = 6;
Mon_Barrier = monomials([x11;x12;x21;x22],[0:degree]);
degree = 6;
Mon_x11 = monomials(x11,[0:degree]);
Mon_x12 = monomials(x12,[0:degree]);       
Mon_x21 = monomials(x21,[0:degree]);
Mon_x22 = monomials(x22,[0:degree]);          
Mon_x12x22 = monomials([x12;x22],[0:degree]); 
Mon_x11x21 = monomials([x11;x21],[0:degree]); 
 Mon_x11x12x21x22 = monomials([x11;x12;x21;x22],[0:degree]); 
Mon_u2 = monomials(u2,[0:degree]);                                                        

%%  ========  lagrange for first condition ================ 
%[prog,L03]=sospolyvar(prog,Mon_x11x12x21x22,'wscoeff'); 
[prog,L031]=sospolyvar(prog,Mon_x12x22,'wscoeff'); 
[prog,L032]=sospolyvar(prog,Mon_x11x21,'wscoeff'); 
% ========  lagrange for second condition(unsafe) ================ 

[prog,Lu31]=sospolyvar(prog,Mon_x11x21,'wscoeff');  [prog,Lu32]=sospolyvar(prog,Mon_x11x21,'wscoeff');  
%[prog,Lu322]=sospolyvar(prog,Mon_x21,'wscoeff');  [prog,Lu323]=sospolyvar(prog,Mon_x21,'wscoeff');  
[prog,Lu33]=sospolyvar(prog,Mon_x12x22,'wscoeff');   [prog,Lu34]=sospolyvar(prog,Mon_x12x22,'wscoeff');    
% ========  lagrange for third condition ================ (\lambda(x1,x2))
[prog,L31]=sospolyvar(prog,Mon_x12x22,'wscoeff');      [prog,L32]=sospolyvar(prog,Mon_x22,'wscoeff');    
[prog,L33]=sospolyvar(prog,Mon_x12x22,'wscoeff');    [prog,L34]=sospolyvar(prog,Mon_x11x21,'wscoeff'); 
 
 

[prog,Lcon]=sospolyvar(prog,Mon_u2,'wscoeff');   

%% 
[prog,Barrier] = sospolyvar(prog,Mon_Barrier,'wscoeff');
% u11 = U_min;
% u12 = U_min;
u11 = U_max;
u12 = U_max;

f_x11 = (1-2*alpha-ae-ah*u11)*x11+ alpha*x12+ ae*Te + ah*Th*u11;
f_x12 = (1-2*alpha-ae-ah*u12)*x12+ alpha*x11+ ae*Te + ah*Th*u12;

f_x21 = (1-2*alpha-ae-ah*u2)*x21+ alpha*x22+ ae*Te + ah*Th*u2;
f_x22 = (1-2*alpha-ae-ah*u2)*x22+ alpha*x21+ ae*Te + ah*Th*u2;

B_f = subs(Barrier,{x11,x12,x21,x22},{f_x11,f_x12,f_x21,f_x22});

%% Lagrange multipliers                                               
%
prog = sosineq(prog,-Barrier-[L031 L032]*g_0+epsilon_1); 

prog = sosineq(prog,Barrier-[Lu31 Lu33]*[g_b1;g_b3]-epsilon_2);
prog = sosineq(prog,Barrier-[Lu32 Lu34]*[g_b1;g_b4]-epsilon_2);
% prog = sosineq(prog,Barrier-[Lu31 Lu322 Lu33]*[g_b1;g_b2;g_b3]-epsilon_2);
% prog = sosineq(prog,Barrier-[Lu32 Lu323 Lu34]*[g_b1;g_b2;g_b4]-epsilon_2);
% B_f<Barrier
prog = sosineq(prog, -B_f+kappa*Barrier-[L33 L34]*g_u-Lcon*U2_all);  
 


% conditions for positiveness of coefficients
prog = sosineq(prog,L031);  
prog = sosineq(prog,L032);  

%prog = sosineq(prog,Lu322);prog = sosineq(prog,Lu323);  
prog = sosineq(prog,Lu31);	prog = sosineq(prog,Lu32); prog = sosineq(prog,Lu33);	prog = sosineq(prog,Lu34);	
prog = sosineq(prog,L31);	prog = sosineq(prog,L32);	 prog = sosineq(prog,L33); prog = sosineq(prog,L34);
prog = sosineq(prog,Lcon);

% call sos solver (requires SeDuMi installed)
prog = sossolve(prog); 

% check the results
SOLV_barrier = sosgetsol(prog,Barrier);
% SOLV1 = sosgetsol(prog,-Barrier-L03*g_0+epsilon_1);  
SOLV1 = sosgetsol(prog,-Barrier-[L031 L032]*g_0+epsilon_1);  
SOLV2 = sosgetsol(prog,Barrier-[Lu31 Lu33]*[g_b1;g_b3]-epsilon_2);      
SOLV3 = sosgetsol(prog,Barrier-[Lu32 Lu34]*[g_b1;g_b4]-epsilon_2);  
% SOLV2 = sosgetsol(prog,Barrier-[Lu31 Lu322 Lu33]*[g_b1;g_b2;g_b3]-epsilon_2);      
% SOLV3 = sosgetsol(prog,Barrier-[Lu31 Lu323 Lu34]*[g_b1;g_b2;g_b4]-epsilon_2);  
SOLV4 = sosgetsol(prog, -B_f+kappa*Barrier-[L33 L34]*g_u-Lcon*U2_all);


echo off;

% check SOS
[P_b1,z_b1] = findsos(SOLV1);
[P_b2,z_b2] = findsos(SOLV2);
[P_b3,z_b3] = findsos(SOLV3);
[P_b4,z_b4] = findsos(SOLV4);


aaa = [length(P_b1),length(P_b2),length(P_b3),length(P_b4)];
mmm = [length(z_b1),length(z_b2),length(z_b3),length(z_b4)]


% show results
Barrier_function = SOLV_barrier


%% test dynamics & plot
bc_fh = matlabFunction(Barrier_function, 'Vars', [x11,x12,x21,x22]);
simu_0819_2;
