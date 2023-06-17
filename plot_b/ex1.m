%Optimization-Based Methods for Nonlinear and Hybrid Systems Verification
%Stephen Prajna...example 1
clear; echo on;
syms x1 x2 ua ub;
vars = [x1; x2];
f = [x1+x2; x1*x2-0.5*x2^2];
%all<=0
Init1=expand((x1-0)*(x1-0.2));
Init2=expand((x1+0.2)*(x1-0));
Unsafe=(x1+1.5)^2+(x2+1.5)^2-0.34;
Inv1=expand((x1+5)*(x1-0.25));
Inv2=expand((x2+5)*(x2-5));
% sosprogram
%initialize the SOS progrsm
prog = sosprogram(vars);
uu4=monomials(vars,0:4);
uu3=monomials(vars,0:3);
uu=monomials(vars,0:0);
% sospolyvar  declare a polynomial variable
%[prog,B] = sospolyvar(prog,uu4);7
[prog,BB] = sospolyvar(prog,uu3);
B_bar = -0.0182176813886769*x1^3 + 0.15511495788369*x1^2*x2 + 0.14401196090601*x1^2 - 0.211669910835658*x1*x2^2 - 0.423621599902095*x1*x2 - 0.196691811266003*x1 + 1.30045827689114*x2^3 + 1.82535404842402*x2^2 - 5.32681484615756*x2 - 1.89178811009891;
[prog,B] = sospolyvar(prog,uu3);
B = BB + B_bar;
%B=(127*x2)/70368744177664 - (3452893951273441*x1)/8796093022208 + (369*x1*x2)/70368744177664 - (37*x1^2)/8796093022208 + (77*x2^2)/70368744177664 - 2851252455641897/17592186044416;
%B>=0 s.t. Init>=0
[prog,p1] = sospolyvar(prog,uu3);
[prog,p2] = sospolyvar(prog,uu3);
% sosineq inequality constraints
prog = sosineq(prog,p1);
B_Init = expand(B + p1*Init1 + p2*Init2);
prog = sosineq(prog,B_Init);


%B<0 s.t. Unsafe<=0
% [prog,e1] = sossosvar(prog,1);
% [prog,q1] = sospolyvar(prog,uu);
% prog = sosineq(prog,q1);
% B_Unsafe = expand(-B-0.01+q1*Unsafe);
% prog = sosineq(prog,B_Unsafe);
% 
% %diff(B,x)>0 s.t. B>=0
% %[prog,r1] = sospolyvar(prog,uu4);
% % %prog = sosineq(prog,r1);
% r1=0;
% [prog,e2] = sossosvar(prog,1);
% [prog,t1] = sospolyvar(prog,uu3);
% prog = sosineq(prog,t1);
% [prog,t2] = sospolyvar(prog,uu3);
% prog = sosineq(prog,t2);
% DB = expand(diff(B,x1)*f(1)+diff(B,x2)*f(2)-0.01+Inv1*t1+Inv2*t2-r1*B);%
% prog = sosineq(prog,DB);
% tic;
% prog = sossolve(prog);
% toc;
% SOLB = sosgetsol(prog,B);
% %SOLR = sosgetsol(prog,r1)
% SOLP1 = sosgetsol(prog,p1);
% SOLQ1 = sosgetsol(prog,q1);
% % E1 = sosgetsol(prog,e1)
% % E2 = sosgetsol(prog,e2)
SOLInit = sosgetsol(prog,B_Init);
% SOLUnsafe = sosgetsol(prog,B_Unsafe);
% SOLDB = sosgetsol(prog,DB);
findsos(SOLInit)
%findsos(SOLUnsafe)
%findsos(SOLDB)
echo off;

