# -*- coding: utf-8 -*-
"""
Created on Thu Sep 07 13:38:57 2017

@author: PC-PRO-FLORIAN
"""
def average_above_zero(list):

    som=0
    n=0
    
    for item in list:
    	if item>0:
    		som += item
    		n += 1
    	elif item==0:
    		print('This value is not positive: '+str(item))
    	else:
    		print('This value is negative '+str(item))
    average = som/n
    print('Positive elements average is '+str(average))
    
def max_value(list):
    
    maxValue = -99999999999999999999
    for item in list:
        if item > maxValue:
            maxValue = item
    print('The max value of the list is '+str(maxValue))
    
def reverse_table(inputList):
    
    list = inputList
    numberOfItem = len(list)
    
    for n in range(0,numberOfItem):
        list.append(list[numberOfItem-n-1])
    for n in range(0,numberOfItem):
        list.remove(list[n])
        
        print(list)
    
input_list=[1,2,3,4,-7]

average_above_zero(input_list)
max_value(input_list)
reverse_table(input_list)

