import turtle
import random
import nltk # type: ignore
from nltk.tokenize import word_tokenize # type: ignore
from nltk.corpus import stopwords # type: ignore
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

    flower_types = ['rose', 'dandelion', 'daisy', 'sunflower', 'lily']
    flower_type = None
    for word in filtered_words:
        if word in flower_types:
            flower_type = word
            break
        elif word.endswith('s') and word[:-1] in flower_types:
            flower_type = word[:-1]
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


def draw_dandelion():
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(50)  
    turtle.end_fill()

    # Reset position
    turtle.right(90)
    turtle.penup()
    turtle.forward(0) 
    turtle.pendown()

    turtle.color('green')
    turtle.pensize(5)
    turtle.forward(150)

    turtle.pensize(1)
    turtle.penup()
    turtle.backward(210)  
    turtle.left(90)  
    turtle.pendown()

    


def draw_daisy():
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


def draw_sunflower():
    turtle.color('yellow')
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


def draw_lily():
    turtle.color('purple')
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

    
def draw_flowers(flower_type, count):
    turtle.speed(0)
    angle = 360 / count
    radius = 200

    draw_function = {
        'rose': draw_rose,
        'dandelion': draw_dandelion,
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
    user_input = input("Please choose your favorite flower and quantity (ex: make me 5 awesome dandelions): ")
    count, flower_type = parse_user_input(user_input)
    if flower_type not in ['rose', 'dandelion', 'daisy', 'sunflower', 'lily']:
        print(f"Invalid flower type '{flower_type}'. Please try again.")
    else:
        draw_flowers(flower_type, count)
