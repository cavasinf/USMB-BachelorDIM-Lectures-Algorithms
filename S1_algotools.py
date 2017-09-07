# -*- coding: utf-8 -*-
"""
Created on Thu Sep 07 13:38:57 2017

@author: PC-PRO-FLORIAN
"""
import numpy

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
        
        
size_rows=10
size_cols=10
myMat=numpy.zeros([size_rows,size_cols], dtype=int)
myMat[1,3]=1

myMat[2:4,5:9]=1
myMat[4:7,7:9]=numpy.ones([3,2])

def roi_bbox(myMat):
    
    print(myMat)
    
    xMin=10
    xMax=0
    yMin=10
    yMax=0
    
    for x in range(10):
        for y in range(10):
            if myMat[y,x]>0:
                if xMin>x:
                    xMin = x
                if xMax<x:
                    xMax=x
                if yMin>y:
                    yMin=y
                if yMax<y:
                    yMax=y
                    
    print("xMin="+str(xMin))
    print("xMax="+str(xMax))
    print("yMin="+str(yMin))
    print("yMax="+str(yMax))
            
    result= ["["+str(xMin)+","+str(yMin)+"]","["+str(xMax)+","+str(yMin)+"]","["+str(xMin)+","+str(yMax)+"]","["+str(xMax)+","+str(yMax)+"]"]
    print(str(result))
    
    
input_list=[1,2,3,4,-7]

average_above_zero(input_list)
max_value(input_list)
reverse_table(input_list)
roi_bbox(myMat)


