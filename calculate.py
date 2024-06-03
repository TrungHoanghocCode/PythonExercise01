# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:33:08 2024

@author: Admin
"""


def calculate(x, y, operation):
    if operation in ['cong' , 'addition' , '+']:
        return x + y
    elif operation in ['tru' , 'subtraction' , '-']:
        return x - y
    elif operation in ['nhan' , 'multiplication' , '*']:
        return x * y
    elif operation in ['chia' , 'division' , '/']:
        if y != 0:
            return x / y
        else:
            return 'In Division, y!=0'
    else:
        return 'Some thing wrong, Pls check operation!'