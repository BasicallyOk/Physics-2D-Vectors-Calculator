import math
import string

run = True

d1 = float(input("First vector?"))
dir1 = str(input("Direction?"))
d2 = float(input("Second Vector?"))
dir2 = str(input("Second Direction?"))

#find d_result only if the movements are perpendicular
d_result = math.sqrt(d1*d1 + d2*d2)

dir_result = math.degrees(math.atan(float(d1/d2)))

#allow many vectors to be in the question (still need to work on calculations for vector direction)
while run == True:
    answer = input("Any more vectors?")
    if answer == "yes":
        d_more = input("?")
        dir_more = input("Direction?")
        d_result = math.sqrt(d_result*d_result + d_more*d_more)
    else:
        run = False

d_result = round(d_result,2)
dir_result = round(dir_result,2)

d = str(d_result)
dir = str(dir_result) #str() does not return any data

print("The resulting vector is: " + d + " [ " + dir1 + " " + dir + " degree " + dir2 + " ]")
