import sys
import math

PI = 3.141592653589793

while True:
    try:
        x1, y1, x2, y2, x3, y3 = map(float, input().split())
    
        a = math.hypot(x2 - x3, y2 - y3)
        b = math.hypot(x3 - x1, y3 - y1)
        c = math.hypot(x1 - x2, y1 - y2)
    
        S = abs((x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1)) / 2.0
        R = a * b * c / (4.0 * S)
        C = 2 * PI * R
    
        print(f"{C:.2f}")

    except: break

