from array import *
import math

 


T = [[0.1, -math.log(0.1)], 
    [2,  -math.log(2)], 
    [0.9,  -math.log(0.9)], 
    [1.01,  -math.log(1.01)],
    [0.999,  -math.log(0.999)],
    [1.0001,  -math.log(1.0001)],
    [0.9999999,  -math.log(0.9999999)],
    [1.00000001,  -math.log(1.00000001)]]
    


imput_ = 1800
calc = imput_
sum = 0


for x in T:
    if x[1] < 0 :
        while calc < 1:
            print( calc ," *" , x[0], " =",  calc * x[0], " ", x[1] )
            calc = calc * x[0]
            sum = sum + x[1]
            
            #print("< 1", x, " " , calc , " " , sum)
            
    else:
        while calc > 1:
            print( calc ," *" , x[0], " =",  calc * x[0], " ", x[1] )
            calc = calc * x[0]
            sum = sum + x[1]
            
            #print("> 1", x, " " ,calc , " " , sum)
 
print(sum)


