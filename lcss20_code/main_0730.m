clc; clear; close all;

% Main code for 2-d vehicle for opacity
% Succesfully found the Barrier with appropriate manually designed controller
% Main code for lcss20 example1


echo on;

%% Parameters
% 2-dimensional system
% x(t+1) = x(t) + v(t) + 0.5*u(t); v(t+1) = v(t) + u(t); y(t) = v(t)
A = [1 1; 0 1];
B = [0.5; 1];
C = [0 1];

% 
c = 1;
delta = 1;
epsilon_1 =1;
epsilon_2 =1.001;  % epsilon_2 >= epsilon_1
kappa = 1 ;     % constant kappa in the last condition

%% SOS Program
% define variables required for SOS program
syms x1 x2 v1 v2 u1;
vars = [x1; x2; v1; v2; u1];

% define lower and upper bounds
X_min = [0; 0];
X_max = [10; 10];
X_0_min = X_min;
X_0_max = X_max;
X_s_min = [0; 0];
X_s_max = [1; 1];
X_ns_min = X_s_max;
X_ns_max = X_max;
V_min = [0; 0];
%V_max = [0.3; 0.3];
V_max = [0.1; 0.1]; 
% U_min = [-0.1; -0.1];
% U_max = [0.1; 0.1];
% U_min = [-0.05; -0.05];
% U_max = [0.05; 0.05]; 
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

% initialize the sum of squares program
prog = sosprogram(vars);

% define monomials
degree = 2;
Mon_Barrier = monomials([x1;x2;v1;v2],[0:degree]);       
Mon_x1 = monomials(x1,[0:degree]);
Mon_x2 = monomials(x2,[0:degree]);       
Mon_v1 = monomials(v1,[0:degree]);
Mon_v2 = monomials(v2,[0:degree]);       
Mon_x1x2 = monomials([x1;x2],[0:degree]); 
Mon_x1v1x2v2 = monomials([x1;x2;v1;v2],[0:degree]); 
Mon_u1 = monomials(u1,[0:degree]);                                                        


% lagrange for first condition
[prog,L01] = sospolyvar(prog,Mon_x1,'wscoeff');
[prog,L02] = sospolyvar(prog,Mon_x2,'wscoeff');     
[prog,L03] = sospolyvar(prog,Mon_x1x2,'wscoeff'); 
[prog,L011] = sospolyvar(prog,Mon_v1,'wscoeff');
[prog,L022] = sospolyvar(prog,Mon_v2,'wscoeff');     


% lagrange for second condition(unsafe)
[prog,Lu1] = sospolyvar(prog,Mon_x1,'wscoeff');
[prog,Lu2] = sospolyvar(prog,Mon_x2,'wscoeff');   
[prog,Lu3] = sospolyvar(prog,Mon_x1x2,'wscoeff');  
[prog,Lu11] = sospolyvar(prog,Mon_v1,'wscoeff');
[prog,Lu22] = sospolyvar(prog,Mon_v2,'wscoeff');   


% lagrange for third condition (\lambda(x1,x2))
[prog,L31] = sospolyvar(prog,Mon_x1,'wscoeff');
[prog,L32] = sospolyvar(prog,Mon_x2,'wscoeff');
[prog,L311] = sospolyvar(prog,Mon_v1,'wscoeff');
[prog,L322] = sospolyvar(prog,Mon_v2,'wscoeff');
[prog,L_con] = sospolyvar(prog,Mon_u1,'wscoeff');  
[prog,L_con1] = sospolyvar(prog,Mon_u1,'wscoeff');  
[prog,L_con2] = sospolyvar(prog,Mon_u1,'wscoeff');

[prog,L33] = sospolyvar(prog,Mon_x1,'wscoeff');
[prog,L34] = sospolyvar(prog,Mon_x2,'wscoeff');
[prog,L333] = sospolyvar(prog,Mon_v1,'wscoeff');
[prog,L344] = sospolyvar(prog,Mon_v2,'wscoeff');
[prog,L35] = sospolyvar(prog,Mon_x1,'wscoeff');
[prog,L36] = sospolyvar(prog,Mon_x2,'wscoeff');    
[prog,L355] = sospolyvar(prog,Mon_v1,'wscoeff');
[prog,L366] = sospolyvar(prog,Mon_v2,'wscoeff');

% third condition B(f(x,u),f(x',u'))
f_x1 = x1 + v1 + 0.5*u1;
f_v1 = v1 + 1*u1;

% f_x1 = x1 + v1*v1 - v1 + u1;
% f_v1 = 2*v1 + u1;

 %u2 = 0.6*x1-0.6*x2+1.2*v1-1.2*v2+u1;
u2 = 0.8*x1-0.8*x2+1.5*v1-1.5*v2+u1;
%u2 = 2*x1-2*x2+2*v1-2*v2+u1;
%u2 =  0.0636*x1-0.0636*x2+0.3568*v1-0.3568*v2;
% u2 =  0.0883*x1-0.0883 *x2+0.4203*v1-0.4203*v2+u1;
% u2 =  0.0605*x1-0.0605*x2+0.3478*v1-0.3478*v2+u1;
% u2 =  0.0030*x1-0.0030*x2+0.0780*v1-0.0780*v2+u1;

f_x2 = x2 + v2 + 0.5*u2;
f_v2 = v2 + 1*u2;
% f_x2 = x2 + v2*v2 - v2 + u2;
% f_v2 = 2*v2 + u2;

[prog,Barrier] = sospolyvar(prog,Mon_Barrier,'wscoeff');
B_f = subs(Barrier,{x1,x2,v1,v2},{f_x1,f_x2,f_v1,f_v2});


% Lagrange multipliers                                               
% B<epsilon_1
prog = sosineq(prog,-Barrier-[L01 L02 L03 L011 L022]*g_0+epsilon_1); 
% B>epsilon_2 
prog = sosineq(prog,Barrier-[Lu1 Lu2 Lu3 Lu11 Lu22]*g_u-epsilon_2);  
% B_f<Barrier
prog = sosineq(prog, -B_f+kappa*Barrier-[L31 L32 L311 L322]*[X1_all;X2_all;V1_all;V2_all]);  

prog = sosineq(prog,U1_all);


% conditions for positiveness of coefficients
prog = sosineq(prog,Barrier);
prog = sosineq(prog,L01);   prog = sosineq(prog,L02);   prog = sosineq(prog,L03);  
prog = sosineq(prog,L011);  prog = sosineq(prog,L022);   
prog = sosineq(prog,Lu1);   prog = sosineq(prog,Lu2);   prog = sosineq(prog,Lu3); 
prog = sosineq(prog,Lu11);	prog = sosineq(prog,Lu22);	
prog = sosineq(prog,L31);	prog = sosineq(prog,L32);	

prog = sosineq(prog,L311);	prog = sosineq(prog,L322);	


% call sos solver (requires SeDuMi installed)
prog = sossolve(prog); 

% check the results
SOLV_barrier = sosgetsol(prog,Barrier);

SOLV2 = sosgetsol(prog, -Barrier-[L01 L02 L03 L011 L022]*g_0+epsilon_1);      
SOLV3 = sosgetsol(prog,  Barrier-[Lu1 Lu2 Lu3 Lu11 Lu22]*g_u-epsilon_2);  
SOLV4 = sosgetsol(prog,  -B_f+kappa*Barrier-[L31 L32 L311 L322]*[X1_all;X2_all;V1_all;V2_all]);


echo off;

% check SOS
[P_b,z_b] = findsos(SOLV_barrier);
[P_b2,z_b2] = findsos(SOLV2);
[P_b3,z_b3] = findsos(SOLV3);
[P_b4,z_b4] = findsos(SOLV4);
% 
% 
aaa = [length(P_b),length(P_b2),length(P_b3),length(P_b4)];
mmm = [length(z_b),length(z_b2),length(z_b3),length(z_b4)]


% show results
Barrier_function = SOLV_barrier


%% test dynamics & plot
bc_fh = matlabFunction(Barrier_function, 'Vars', [x1,x2,v1,v2]);
% test_simu_0730;
test_simu_0818;
