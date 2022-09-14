import math
from itertools import combinations




def classify_triangle(a,b,c):
    if math.sqrt((a*a) + (b*b))== c or math.sqrt((a*a) + (c*c))== b or math.sqrt((c*c) + (b*b))== a: 
        print( "Right Triangle")

    if a == b == c:
        return "Equilateral Triangle"
    
    elif a != b !=c:
        return "Isosceles Triangle"
    
    else:
        return 



classify_triangle(5,12,13)