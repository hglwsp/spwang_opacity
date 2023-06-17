function [ out] = sigmoid( x )
%   consider u with sigmoid active function
% sigmoid = 1 / (1 + e^(-x))
res = 1 / (1 + exp(-x));

out = res;


end

