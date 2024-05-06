# Enter your code here. Read input from STDIN. Print output to STDOUT
# calculate H
# divide h/2
# the angle should be sin((h/2)/BC) #in the case it is equalleteral
import cmath as m

AB = int(input())
BC = int(input())

H = m.sqrt(AB**2 + BC**2)

# d = round(((m.asin((H/2)/BC).real) * (180/m.pi)) % 360)

# get the length of the lind dropped from M onto BC called MD

# get angle BCA
BAC = m.asin(AB/H).real

#get angle CMD
#CMD = (m.pi/4) - BAC

# use the length of MC and all the angles in MDC to get the length of MD
MD = m.sin(BAC) * H/2

DC = m.sqrt((H/2) ** 2 - MD**2)

BD = BC - DC


d = round((m.atan(MD/BD).real * (180/m.pi)) % 360)


print(f"{d}\N{DEGREE SIGN}")