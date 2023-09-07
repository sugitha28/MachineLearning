import numpy as np

#CREATING ARRAY USING NUMPY
array = np.array([67,90,56,43,2,8,9])
print(array)

#PRINTNG THE NUMBER OF ELEMENTS IN THE ARRAY
print(array.shape)

#CREATING THE ARRAY IN RANGE 0 TILL 9
array2=np.arange(10)
print(array2)

#CREATING ARRAY IN RANGE FROM 0 TILL 99 WITH STEP 7
ar3=np.arange(0,100,7)
print(ar3)

#CREATING ARRAY FULL OF ZERO 
ar4=np.zeros(10)
print(ar4)

#CREATING ARRAY A 2D ARRAY R=7 C=5 FULL OF ZERO
ar5=np.zeros((7,5))
print(ar5)

#CREATING A 1D ARRAY OF SIZE 8 FULL OF 3
ar6=np.full((8),3)
print(ar6)

#CREATING A 2D ARRAY OF R=2 C=5 FULL OF 7
ar7=np.full((2,5),7)
print(ar7)

#CONVERTING A LIST INTO NUMPY ARRAY
my_list=[2,7,9,6,23]
ar8=np.array(my_list)
print(ar8)
