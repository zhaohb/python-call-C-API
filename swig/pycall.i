%module pycall
%{
extern int plus(int a, int b);
extern int subtract(int a, int b);
extern int multiple(int a, int b);
extern int divide(int a, int b);
%}

extern int plus(int a, int b);
extern int subtract(int a, int b);
extern int multiple(int a, int b);
extern int divide(int a, int b);
