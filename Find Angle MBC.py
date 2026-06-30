#Find Angle MBC
import math

AB = int(input())
BC = int(input())

angle = math.degrees(math.atan(AB / BC))
print("{}{}".format(round(angle), chr(176)))