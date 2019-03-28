#!/usr/bin/env python
# coding=utf-8
import pycall

print(pycall.plus(1,1))
print(pycall.subtract(4,1))
print(pycall.multiple(4,2))
print(pycall.divide(10,2))

a=pycall.Student('zhaohb', 99)
b=pycall.setinfo(a)
print(b)
