# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 18:01:17 2019

@author: Prancis Fayat
"""

import numpy as np
import math as mt

def circle(x1,y1,x2,y2,x3,y3):
    a = np.array([(x1,y1,1), (x2,y2,1), (x3,y3,1)])
    b = np.array([(-1*(x1**2 + y1**2)),(-1*(x2**2 + y2**2)),(-1*(x3**2 + y3**2))])
    DEF = np.linalg.inv(a).dot(b)
    d = int(DEF[0])
    e = int(DEF[1])
    f = int(DEF[2])
    vectorDEF = np.array((d,e,f))
    h = -(d/2)
    k = -(e/2)
    r =  mt.sqrt(-f + h**2 + k**2)

    print('center is at ', "(",h, ",", k,")" )
    print('radius is = ', round(r, 4))
    print('vector DEF: ', vectorDEF)
    