#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int plus(int a, int b)
{
    return a+b;
}

int subtract(int a, int b)
{
    return a-b;
}

int multiple(int a, int b)
{
    return a*b;
}

int divide(int a, int b)
{
    return a/b;
}

typedef struct Student
{  
    char* name;  
    int age;  
}Student;  

Student * setinfo(Student *q)
{
    Student * p = (Student *)malloc(sizeof(Student));   
    strcpy(p->name, q->name);  
    p->age = q->age;  
    printf("name:%s\n", p->name);
    printf("age:%d\n", p->age);

    return p;   
}
