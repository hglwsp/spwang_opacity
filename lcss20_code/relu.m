function [ out ] = relu( x )
%   consider u with leakyrelu active function
if x >= 0
   res = x
end
if x <= 0
   res = 0;
end

out = res

end



