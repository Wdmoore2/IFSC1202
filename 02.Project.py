a =(float(input ("Enter Side 1:")))
b = (float(input ("Enter Side 2:") ))
c = (float)(input ("Enter Side 3:") )
s = (float(a + b + c)/2)
import math
answer = math.sqrt (s * (s-a)* (s-b)*(s-c))
area = ("Area: ") +str(answer)
print (area)