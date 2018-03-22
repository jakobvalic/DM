clc

%Vaja 3 z dne 1. 3.
c = [15;50;2;0;0;0];
A = [0,0,0,1,0,0; 1,1,1,1,0,0; 0,1,-10,0,-1,0; -1,0.25,0,0.25,0,-1];
b = [0.2;1;0;0];

%Parametri za numerično računanje
lb = [0,0,0,0,0,0];
ub = [1,1,1,1,1,1];
[x,f]=glpk(c,A,b,lb,ub,"SSSS") %S pomeni, da v vseh enačbah nastopajo enačaji (privzeto)
%[x,f]=glpk(c,A,b)