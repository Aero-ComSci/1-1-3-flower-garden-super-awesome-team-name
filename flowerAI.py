import turtle
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
import math

nltk.download('punkt')
nltk.download('stopwords')

def parse_user_input(user_input):
    tokens = word_tokenize(user_input.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in tokens if word.isalpha() and word not in stop_words]
    
    number = None
    numbers_in_input = re.findall(r'\d+', user_input)
    if numbers_in_input:
        number = int(numbers_in_input[0])

    flower_types = ['rose', 'tulip', 'daisy', 'sunflower', 'lily']
    flower_type = None
    for word in filtered_words:
        if word in flower_types:
            flower_type = word
            break

    if number is None:
        number = 1

    if flower_type is None:
        flower_type = 'rose'
    
    return number, flower_type

def draw_rose():
    turtle.color('red')
    turtle.begin_fill()

    for _ in range(6):  
        turtle.circle(50, 60)  
        turtle.left(120)
        turtle.circle(50, 60)
        turtle.left(60)

    turtle.end_fill()

    
    turtle.right(90)
    turtle.penup()
    turtle.forward(60) 
    turtle.pendown()

    turtle.color('green')
    turtle.pensize(5)
    turtle.forward(150)

    
    turtle.pensize(1)
    turtle.penup()
    turtle.backward(210)  
    turtle.left(90)  
    turtle.pendown()


def draw_tulip():
    turtle.color("pink")
    turtle.begin_fill()
    
    
    turtle.penup()
    turtle.goto(0, 0)  
    turtle.pendown()
    turtle.setheading(0)  
    
   
    turtle.circle(40, 180)
    
    
    turtle.setheading(-90)  
    turtle.forward(80)    
    turtle.setheading(180) 
    turtle.circle(-40, 180) 
    turtle.setheading(90)  
    turtle.forward(80)     
    
    turtle.end_fill()
    
    turtle.color('green')
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(0, -80)  
    turtle.setheading(-90)  
    turtle.pendown()
    turtle.forward(100)  
    
    
    turtle.pensize(1)
    turtle.penup()
    turtle.goto(0, 0)  
    turtle.setheading(0)  
    turtle.pendhown()



def draw_daisy():
    turtle.color("yellow")
    turtle.begin_fill()
    for _ in range(8):
        turtle.forward(40)
        turtle.left(45)
    turtle.end_fill()


def draw_sunflower():
    turtle.color("orange")
    turtle.begin_fill()
    for _ in range(12):
        turtle.forward(60)
        turtle.left(30)
    turtle.end_fill()


def draw_lily():
    turtle.color("purple")
    turtle.begin_fill()
    
    
    for _ in range(6):
        turtle.forward(60)  
        turtle.right(120)
        turtle.forward(60) 
        turtle.left(60)  

    turtle.end_fill()

    turtle.color('green')
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(0, -60)  
    turtle.setheading(-90)  
    turtle.pendown()
    turtle.forward(100)  

    turtle.pensize(1)
    turtle.penup()
    turtle.goto(0, 0) 
    turtle.setheading(0)  
    turtle.pendown()

def draw_flowers(flower_type, count):
    turtle.speed(0)
    angle = 360 / count
    radius = 200  

    draw_function = {
        'rose': draw_rose,
        'tulip': draw_tulip,
        'daisy': draw_daisy,
        'sunflower': draw_sunflower,
        'lily': draw_lily
    }.get(flower_type, draw_rose)  

    for i in range(count):
        turtle.penup()
        x = radius * math.cos(math.radians(angle * i))
        y = radius * math.sin(math.radians(angle * i))
        turtle.goto(x, y)
        turtle.pendown()
        draw_function() 
        turtle.penup()  
        turtle.goto(x, y) 

    turtle.done()

if __name__ == "__main__":
    user_input = input("Please specify the number and type of flowers (e.g., 'Draw 5 roses'): ")

    count, flower_type = parse_user_input(user_input)

    draw_flowers(flower_type, count)
