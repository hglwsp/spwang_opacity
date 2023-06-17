figure

[x,y,t] = meshgrid(-3:0.05:3,-3:0.05:3,0:0.05:10);
v =30.56.*x+13.8.*y-.4614.*t+.5454.*x.^3-1.713.*x.*y.*t-.4558.*x.*y.^2.*t+.1343.*x.*y.*t.^2+.484.*x.^2.*y.*t+7.637-7.288.*y.^2+5.05.*x.^4+1.786.*x.^2+64.26.*y.^3-4.54.*y.^4+.2091.*t.^2-0.275e-1.*t.^3+0.1523e-2.*t.^4+21.68.*x.^3.*y+14.61.*x.^2.*y.^2+52.57.*x.^2.*y+19.61.*x.*y.^3+42.89.*x.*y.^2-12.28.*x.*y-.591.*x.^3.*t+0.4251e-1.*x.^2.*t.^2-.7446.*x.^2.*t+0.3146e-2.*x.*t.^3+0.2478e-1.*x.*t.^2+.7894.*x.*t+1.641.*y.^3.*t+.578.*y.^2.*t.^2-5.439.*y.^2.*t-0.9679e-2.*y.*t.^3+.5196.*y.*t.^2-3.068.*y.*t;
B = patch(isosurface(x,y,t,v,0),'FaceColor','c','EdgeColor','none');

[x,y,z] = meshgrid(-3:0.05:3,-3:0.05:3,0:0.001:0.1);
v2 =(x-1.5).^2+y.^2-0.25 ;
init = patch(isosurface(x,y,z,v2,0),'FaceColor','g','EdgeColor','none');

%[x1,x2,t] = meshgrid(-2:0.01:2,-2:0.01:2,19.9:0.001:20);
%v2 =(x1).^2+(x2).^2-(3/5).^2 ;
%G = patch(isosurface(x1,x2,t,v2,0),'FaceColor','b','EdgeColor','none');

[x,y,z] = meshgrid(-3:0.05:3,-3:0.05:3,0:0.05:10);
v2 =(x+1).^2+(y+1).^2-1.18.^2 ;
Unsafe = patch(isosurface(x,y,z,v2,0),'FaceColor','r','EdgeColor','none');

view(3)
%camlight %光影效果
axis equal tight
grid on