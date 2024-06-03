# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:32:29 2024

@author: Admin
"""

from calculate import calculate

def main():
    try:
        x = float(input("Enter the first number (x): "))
        y = float(input("Enter the second number (y): "))
        operation = input("Enter the operation (Cong/Addition/+, Tru/Subtraction/-, Nhan/Multiplication/*, Chia/Division//): ").strip().lower()
        
        result = calculate(x, y, operation)
        
        print(f"The result is: {result}")
    except ValueError:
        print("Some thing wrong, Pls check x, y (number) !")

if __name__ == "__main__":
   main()