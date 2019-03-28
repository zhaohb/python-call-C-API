%module pycall
%{
extern int plus(int a, int b);
extern int subtract(int a, int b);
extern int multiple(int a, int b);
extern int divide(int a, int b);

typedef struct Student  
{  
    char* name;  
    int age;  
}Student;  
Student * setinfo(Student *q);

%}

typedef struct Student
{  
    char* name;  
    int age;  
}Student;  

%extend Student{
    Student(char* name, int age){
        Student * p = (Student *)malloc(sizeof(Student));
        p->name = name;
        p->age = age;
        
        return p;
    };
};

Student * setinfo(Student *q);
extern int plus(int a, int b);
extern int subtract(int a, int b);
extern int multiple(int a, int b);
extern int divide(int a, int b);
