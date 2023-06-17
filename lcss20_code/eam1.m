%Optimization-Based Methods for Nonlinear and Hybrid Systems Verification
%Stephen Prajna...example 1
clear; echo on;
syms x1 x2 ua ub;
vars = [x1; x2];
f = [-x1+x1*x2; x2-x1*x2];
%all<=0
Init1=expand((x1-0)*(x1-0.2));
Init2=expand((x1+0.2)*(x1-0));
B_bar = -0.0182176813886769*x1^3 + 0.15511495788369*x1^2*x2 + 0.14401196090601*x1^2....
- 0.211669910835658*x1*x2^2 - 0.423621599902095*x1*x2 - 0.196691811266003*x1 ...
    + 1.30045827689114*x2^3 + 1.82535404842402*x2^2 - 5.32681484615756*x2 ...
    - 1.89178811009891;

prog = sosprogram(vars);
uu4=monomials(vars,0:4);
uu2=monomials(vars,0:2);
uu=monomials(vars,0:0);
%[prog,B] = sospolyvar(prog,uu4);
[prog,B] = sospolyvar(prog,uu2);
%B=(127*x2)/70368744177664 - (3452893951273441*x1)/8796093022208 + (369*x1*x2)/70368744177664 - (37*x1^2)/8796093022208 + (77*x2^2)/70368744177664 - 2851252455641897/17592186044416;
%B>=0 s.t. Init<=0
[prog,p1] = sospolyvar(prog,uu);
[prog,p2] = sospolyvar(prog,uu);
prog = sosineq(prog,p1);
prog = sosineq(prog,p2);
% B_Init = expand(B + B_bar+p1*Init1+p2*Init2);
% prog = sosineq(prog,B_Init);

%B<0 s.t. Unsafe<=0
% [prog,e1] = sossosvar(prog,1);
% [prog,q1] = sospolyvar(prog,uu);
% prog = sosineq(prog,q1);
% B_Unsafe = expand(-B-0.01+q1*Unsafe);
% prog = sosineq(prog,B_Unsafe);

%diff(B,x)>0 s.t. B>=0
%[prog,r1] = sospolyvar(prog,uu4);
% %prog = sosineq(prog,r1);
% r1=0;
% [prog,e2] = sossosvar(prog,1);
% [prog,t1] = sospolyvar(prog,uu2);
% prog = sosineq(prog,t1);
% [prog,t2] = sospolyvar(prog,uu2);
% prog = sosineq(prog,t2);
% DB = expand(diff(B,x1)*f(1)+diff(B,x2)*f(2)-0.01+Inv1*t1+Inv2*t2-r1*B);%
% prog = sosineq(prog,DB);
tic;
prog = sossolve(prog);
toc;
%solve
SOLB = sosgetsol(prog,B)
%SOLR = sosgetsol(prog,r1)
SOLP1 = sosgetsol(prog,p1)
SOLP2 = sosgetsol(prog,p2)
% SOLQ1 = sosgetsol(prog,q1)
% E1 = sosgetsol(prog,e1)
% E2 = sosgetsol(prog,e2)
% SOLInit = sosgetsol(prog,B_Init)
% SOLUnsafe = sosgetsol(prog,B_Unsafe)
% SOLDB = sosgetsol(prog,DB)
% findsos(SOLInit)
% findsos(SOLUnsafe)
% findsos(SOLDB)
echo off;


