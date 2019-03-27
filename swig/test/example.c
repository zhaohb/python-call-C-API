/*************************************************************************
	> File Name: example.c
	> Author: 
	> Mail: 
	> Created Time: 2019年03月27日 星期三 17时19分48秒
 ************************************************************************/

#include<stdio.h>
#include <time.h>
double My_variable = 3.0;

int fact(int n) 
{
    if (n <= 1) 
        return 1;
    else 
        return n*fact(n-1);
}
int my_mod(int x, int y) 
{
    return (x%y);
}

char *get_time()
{
    time_t ltime;
    time(&ltime);
    return ctime(&ltime);
}
