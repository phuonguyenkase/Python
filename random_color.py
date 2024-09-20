import random
import turtle as t
class Random_color:
    def __init__(self):
        t.colormode(255)

    def random_color(self): #function
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        random_color = (r, g, b)  # tuple
        return random_color
