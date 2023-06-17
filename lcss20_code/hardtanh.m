function [ out ] = hardtanh( x )

if x >= 0.04
   res = 0.04;
end
if x <= -0.04
   res = -0.04;
end
if x <= 0.04 && x >= -0.04
   res = x;
end

out = res


end

