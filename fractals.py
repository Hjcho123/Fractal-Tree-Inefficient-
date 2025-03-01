import turtle
import random

branches = {}
branchangles = {}
go =200
max_distance=go
distance = max_distance
turtles_operated = 1
start =1
angle = 0
count = 0
point = 2

repetitions = 100
turtle.colormode(255)

turtle.bgcolor("black")
for numbers in range(1,repetitions):
  
  
  for turtles in range(start,start + turtles_operated):
    distance =max_distance/(random.random()+1)
    turn = random.randint(1,25)
    turtle_name = "turtle"+str(turtles)
  
    turtle_name = turtle.Turtle()
    turtle_name.hideturtle()
    turtle_name.width(1)
    turtle_name.pencolor("white")
    turtle_name.speed(0)
    turtle_name.up()
    turtle_name.goto(0,-450)
    turtle_name.down()
    turtle_name.seth(90)
    
    if numbers ==2 :
      turtle_name.width(1)
      x,y = branches[start-1]
      turtle_name.up()
      turtle_name.goto(x,y)
      turtle_name.down()
      if angle%2 != 0:
        turtle_name.left(turn*(numbers-1))
      elif angle%7 ==0:
        turtle_name.right(0)
      else:
        turtle_name.right(turn)
    if numbers > 2:
      turtle_name.width(1)
      count+=1
      x,y = branches[point]
      turtle_name.up()
      turtle_name.goto(x,y)
      turtle_name.down()
      degree = branchangles[point] 
      if angle%2 != 1:
        turtle_name.right(degree-turn)
      elif angle%7 ==0:
        turtle_name.right(0)
      else:
        turtle_name.right(degree+turn)
      if count%2==0:
        point+=1



        
   
 
   
    if max_distance<=go/15:
      
      turtle_name.dot(3,"deep sky blue")
     
      
           
      
    else:
      turtle_name.forward(distance)
    position = turtle_name.pos()
    branches[turtles] = position
    branchangles[turtles] = -(turtle_name.heading()-90)
    angle +=1
    
    
    
  start +=turtles_operated
  turtles_operated*=2
  max_distance /= 1.4
  print("New Max: " + str(max_distance))
 
  
    
  
  
turtle.up()
turtle.goto(200,-200)
turtle.color("red","red")
turtle.down()
turtle.dot(100)
  
turtle.done()

