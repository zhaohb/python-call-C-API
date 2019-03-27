# coding=utf-8

import ctypes
from ctypes import *

libpath='./libpycall.so'

def loadlib():
    #通过ctypes加载动态库，返回动态库的对象
    lib = ctypes.cdll.LoadLibrary(libpath)
    return lib

def plus(a, b):
    lib = loadlib()
    #通过lib调用动态库中具体的接口
    return lib.plus(a, b)

def subtract(a, b):
    lib = loadlib()
    #通过lib调用动态库中具体的接口
    return lib.subtract(a, b)

def multiple(a, b):
    lib = loadlib()
    #通过lib调用动态库中具体的接口
    return lib.multiple(a, b)

def divide(a, b):
    lib = loadlib()
    #通过lib调用动态库中具体的接口
    return lib.divide(a, b)


#如果要在python中定义一个c类型的结构体，需要定义一个类，该类必须
#继承ctypes.Structure

class StructTest(Structure):
    #定义名为_fields_属性，并赋值，在这里描述具体结构体的成员
    _fields_ = [("name", c_char * 20), ("age", c_int)]

def testfunction():
    #返回值是结构体的形式
    lib = loadlib()
    #指定testfunction接口的返回值的类型（貌似只有涉及到结构体操作时才需要指定）
    lib.testfunction.restype = POINTER(StructTest)
    p = lib.testfunction()
    print(p.contents.name)
    print(p.contents.age)

def setinfo(name, age):
    #参数是结构体的形式,并且返回值也是结构体
    lib = loadlib()
    
    student = StructTest()
    student.name = bytes(name, 'gb2312')
    student.age = age

    lib.setinfo.restype = POINTER(StructTest)
    
    p = lib.setinfo(byref(student))
    print(p.contents.name)
    print(p.contents.age)

#--------------------------------------------------------------------------------#
#结构体的嵌套现在不做具体的例子
#--------------------------------------------------------------------------------#


if __name__ == '__main__':
    print(plus(3, 1))
    print(subtract(3, 1))
    print(multiple(3, 1))
    print(divide(6, 2))
    testfunction()
    setinfo("tony", 22)
