#!/usr/bin/env python
# VOLGA, 2022-10-26, ovekilova@gmail.com
# Короткий скрипт питонюка который берет сколько надо входных OSZICAR, считывает
#из них все E0 по порядку и определяет среднее
#при этом можно выкидывать сколько хочешь сначала
# а в идеале и ранин эверадж с заданным шагом
import math
import matplotlib.pyplot as plt
import re
#from optparse import OptionParser
import argparse

#parser = OptionParser()
#parser.add_option("-h", help="Write a header line",
#                  action="store_true", dest="header", default=False)


#file = "OSZICAR.2"
#firstStep = 10
#numStep = 500
file_test = input("Enter OSZICAR filename/names separated with space: ")
try :
    a = re.findall('(.+)-n',file_test)[0]
    file_list = a.split()
except :
    try :
        a = re.findall('(.+)-f',file_test)[0]
        file_list = a.split()
    except :
        a = file_test
        file_list = a.split()
#print(a)
#file_list = a.split()
print('reading',file_list)


with open('OSZICAR_main', 'w') as outfile : # with open - you don't have to close
    for fname in file_list :
        with open(fname) as infile :
            for line in infile:
                outfile.write(line)


energyList = list()
try :
    fhand = open('OSZICAR_main')
except :
    print('no such file')
    print('opening OSZICAR.1')
    fhand = open('OSZICAR.1')

count = 0
count2 = 0
for line in fhand :
    line = line.strip()
    if "E0" in line :
        linelist = line.split()
        E0 = float(linelist[8])
        count2 = count2 + 1
        if E0 < 0 :
            energyList.append(E0)
            count = count + 1
#print('energylist', energyList)
try :
    numStep = int(re.findall('-n\s([0-9]+)',file_test)[0])
except :
    numStep = count
    print('using the default number of steps, all: ',numStep)
try :
    firstStep = int(re.findall('-f\s([0-9]+)',file_test)[0])
except :
    firstStep = 0
    print('starting from ',firstStep,' interation')

print('numstep', numStep)
print('Total number of iterations in file', count2)
print('Total number of iterations with E0 < 0', count)
if numStep > count :
    numStep = count - firstStep
else :
    numStep = numStep - firstStep
#print('NUMSTEP', numStep)
print("Averaging over", numStep, "steps and skipping first ", firstStep, "steps" )
if firstStep > 1 :
    del energyList[:firstStep-1]
#print(energyList)
del energyList[numStep:]

#print('energylist', energyList)

avE0 = sum(energyList)/numStep
print("Average E0 = ", avE0, " eV")

exit()
