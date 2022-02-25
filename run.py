import turtle     
from sympy.ntheory.primetest import isprime    

def square () :    
    step = 1  
    nums = 1    
    counter = 0   

    screen = turtle.Screen() 
    screen.setup(width = 1.0 , height = 1.0) 

    t = turtle.Turtle()        
    t.screen.bgcolor("black")  
    t.color("white") 
    t.penup() # remove lines 
    t.hideturtle()  
    turtle.tracer(0,0)  # remove animation 
    for i in range (250) :           
        for j in range (step) :     
            if isprime(nums) :   
                t.dot(4)     
            t.forward(5)     
            nums += 1     
            counter += 1 
        if step == counter :  
            counter = 0 
            t.left(90) 
            if t.heading() in (90, 270):
                step += 1     

if __name__ == "__main__" : 
    square() 


input()





