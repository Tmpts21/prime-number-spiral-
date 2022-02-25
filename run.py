import turtle     
from sympy.ntheory.primetest import isprime 


t = turtle.Turtle()      
side = 5 
step = 1  
nums = 1   
t.hideturtle()
for i in range (200) :        
    for j in range (step) :     
        if isprime(nums) :   
            t.dot(4)  
        t.forward(4)     
        nums += 1 
    t.left(90)
    step += 1   
    nums += 1  

t.clear() 

   

input() 



