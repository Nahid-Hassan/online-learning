import cProfile
import re

def add():
    a = 100
    b = 192

    print(a + b)

cProfile.run('add()')
