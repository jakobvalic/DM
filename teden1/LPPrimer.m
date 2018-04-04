%
%  Testiranje lineranega programiranja min(x.c) pri pogoju Ax >= b in 
%  0 <= x <= 100
%
%  n neznank, m ena�b
%  Naklju�na generacija podatkov
%
n = 500
m=n/2
c=randi([-10,10],n,1);
b=randi([-10,10],m,1);
a=randi([-10,10],m,n)./randi([1,10],m,n);
% koda za neenakost
ctype(1:m)=76; %znak za neenakost
% spodnja meja, zgornja meja
lb = zeros(n,1);
ub(1:n) = 100;
[t1,u1,s1]=cputime();
[x,f]=glpk(c,a,b,lb,ub, char(ctype));
[t2,u2,s2]=cputime();
u2-u1
f