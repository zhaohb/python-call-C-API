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

//上面是对接口的封装，不涉及到指针和结构体操作
//------------------------------------------------------------
//下面在C语言中实现结构体操作，在python中实现对C结构体的调用

typedef struct StructTest  
{  
    char name[20];  
    int age;  
}Student;  

Student * testfunction()    // 返回结构体指针  
{   
    Student * p = (Student *)malloc(sizeof(Student));   
    strcpy(p->name, "Joe");  
    p->age = 20;  

    return p;   
}  

Student * setinfo(Student *q)
{
    Student * p = (Student *)malloc(sizeof(Student));   
    strcpy(p->name, q->name);  
    p->age = q->age;  

    return p;   
}

char * printinfo(Student * p)
{
    printf("name:%s\t age:%d\n", p->name, p->age);
    char *data = "Student info had export!";
    return data;
}
