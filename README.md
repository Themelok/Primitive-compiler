# Primitive-compiler
Example of simplest compiler, including lexer and parser. It can be used for problem oriented purposes such as Integration of differential equations systems.

Some usage examples

Begin;
Expr: dx =a*x*(1-x/e-d*(y/3))+x, dy =b*y*(1-y/m-c*(x/4))+y;
Vars0: x=10, y=145;
Coeff: a=0.03, b=0.06, c=0.01, d=0.5, e=5.0, m=4.0;
Step: 0.09;
Range: [0.,4];
Method: Euler;
End;


Begin;
Expr: dx=m-u*x, dy=u*x+ga-ba*y+1;
Vars0: x=15, y=16;
Coeff: m=0.01, ga=0.02, u=0.06, ba=0.07;
Step: 0.1;
Range: [0.,100];
Method: Euler;
End;
