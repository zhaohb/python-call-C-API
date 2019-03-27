#!/bin/bash
swig -python pycall.i
gcc -c -fPIC pycall.c pycall_wrap.c -I/usr/include/python3.5
ld -shared pycall.o pycall_wrap.o -o _pycall.so

