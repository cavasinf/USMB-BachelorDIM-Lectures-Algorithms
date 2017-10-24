# -*- coding: utf-8 -*-
"""
Created on Thu Sep 07 13:38:57 2017

@author: PC-PRO-FLORIAN
"""
import numpy
from random import randint

def average_above_zero(list):
    
    print("===== AVERAGE ZERO =====")

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
    return average
        
def max_value(list):
    print("===== Max Value =====")
    
    maxValue = -99999999999999999999
    for item in list:
        if item > maxValue:
            maxValue = item
    print('The max value of the list is '+str(maxValue))
    return maxValue
    
def reverse_table(inputList):
    print("===== Reverse Table =====")
    print(inputList)
    print("became")
    list = inputList
    numberOfItem = len(list)
    
    for n in range(0,numberOfItem):
        list.append(list[numberOfItem-n-1])
    for n in range(0,numberOfItem):
        list.remove(list[n])
        
    print(list)
    return list
        
        
size_rows=10
size_cols=10
myMat=numpy.zeros([size_rows,size_cols], dtype=int)
myMat[1,3]=1

myMat[2:4,5:9]=1
myMat[4:7,7:9]=numpy.ones([3,2])

def roi_bbox(myMat):
    
    print("===== BBox =====")
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
    
def random_fill_sparse(Table,vfill):
   print(vfill)

def remove_whitespace(stringToParse):
    print("===== Remove white space =====")
    """for i in range(len(stringToParse)):
        if stringToParse[i] == ' ':
            stringToParse[i].remove()
    """
    stringToParse = stringToParse.replace(' ','')
    print(stringToParse)
    
def shuffle(listToSelectRandom):
    print("===== Shuffle =====")
    sizeOfListe = len(listToSelectRandom)
    print(listToSelectRandom[randint(0,sizeOfListe)-1])
    
def dice_game(numberOfPlayer):
    print("===== THE DICE GAME =====")
    playerWhoWin = 0
    onePlayerWin = False
    maxTurn = numberOfPlayer
    actualTurn = 1
    numberOfTurn = 0
    scoreList = [0] * numberOfPlayer
    while onePlayerWin == False :
        randomDice = randint(1,6)
        if randomDice > 1:
            scoreList[actualTurn-1] = scoreList[actualTurn-1]+randomDice
        if actualTurn < maxTurn:
            actualTurn = actualTurn +1
        else:
            actualTurn = 1
        numberOfTurn = numberOfTurn +1
        if scoreList[actualTurn-1]> 99:
            onePlayerWin = True
            playerWhoWin = actualTurn
    print ("The Player number "+str(playerWhoWin)+" win with "+str(scoreList[playerWhoWin-1])+" points")
    print(scoreList)
        
def sort_selective(inputList):
    print("=====SORT SELECTIVE =====")
    alist = inputList
    for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
    print(alist)
            
        
    
def sort_bubble(inputList):
    print("===== SORT BUBBLE =====")
    alist = inputList
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    print(alist)


input_list=[1,0,3,9,4,-7]

average_above_zero(input_list)
max_value(input_list)
reverse_table(input_list)
roi_bbox(myMat)
random_fill_sparse("Table",input_list)
remove_whitespace("Je ne sais pas quoi mettre dedans")
shuffle(input_list)
dice_game(3)
sort_selective(input_list)
sort_bubble(input_list)
print("------ FIN --------")

