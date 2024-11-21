#!/usr/bin/env python3


import sys 
if len(sys.argv) != 1:
    print("none")
else:
    for i in range(0,11):
        show = (f"Table de {i} : {0*i} {1*i} {2*i} {3*i} {4*i} {5*i} {6*i} {7*i} {8*i} {9*i} {10*i}")
        print(show)