# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
"""
MODULE DOCSTRING
"""
import math
XC1 = 4
YC1 = 4.25

XC2 = 53
YC2 = -5.35

def circle_dis(XC1, YC1, XC2, YC2):
    # Calculate the distance between the two circle
    distance = math.sqrt((XC1-XC2)**2 + (YC1 - YC2)**2)
    print('distance', distance)
# *** somewhere else in your program ***
XA = -36
YA = 97

XB = .34
YB = .91

def vec_lens(XA, YA, XB, YB):
    # calcualte the length of vector AB vector which is a vector between A and B points.
    length = math.sqrt((XA-XB)*(XA-XB) + (YA-YB)*(YA-YB))
    print('length', length)

print(circle_dis(XC1, YC1, XC2, YC2))
print(vec_lens(XA, YA, XB, YB))