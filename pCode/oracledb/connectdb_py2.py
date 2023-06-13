#!/usr/bin/env python3
"""
Connect to database using python2
"""
import sys
import os
import platform

ext_lib3 = '/home/harsh/pCode/venv3/lib/python3.10/site-packages'
ext_lib2 = '/home/harsh/pCode/venv2/lib/python2.7/site-packages'
py_version = platform.python_version()
print('python version: {}'.format(py_version))

if py_version.startswith('2'):
    sys.path.append(ext_lib2)
else:
    sys.path.append(ext_lib3)
import cx_Oracle