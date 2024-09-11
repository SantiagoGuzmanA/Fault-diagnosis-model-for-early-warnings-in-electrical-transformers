function Ri = FDM_correlation_coef(i1,i2)
m = length(i1);

num = i1'*i2 - ((1/m)* sum(i1) * sum(i2));
den = sqrt(i1'*i1 - (1/m)*(sum(i1))^2) * sqrt(i2'*i2 - (1/m)*(sum(i2))^2);
Ri = num/den;