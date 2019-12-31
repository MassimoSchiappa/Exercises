# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 17:05:39 2019

@author: Massimo
"""

testlist = [1,2,[5,7,[5,0]],[7,[1,2,3,4,5,[1,4,7]],3]]
flattenlist = []


def flatten_intarray(iarray):
    """ This function flatten an arbitrary nested integer array """    
    if type(iarray) is int:
        flattenlist.append(iarray)
    else:       
        for x in iarray:    
            print(x)
            flatten_intarray(x)

    
    


flatten_intarray(testlist)
    
print('original is:')
print(*testlist,sep = ",")
print('flattened is :')
print(*flattenlist,sep = ",")