#!/usr/bin/env python
# VOLGA, 2022-11-4, ovekilova@gmail.com
# The program takes several OSZICAR files, reads all E0 from them in the order
# of the file insertion. One can cut any number of steps from the beguining and
# calculate average energy. Idially also calculate running average with given step


import math
import matplotlib.pyplot as plt
import re
import argparse

parser = argparse.ArgumentParser(description='insert averaging paramenters')
parser.add_argument('-f', '--fir_step', type=int, metavar='', help='number of step to start averaging from')
parser.add_argument('-n', '--num_steps', type=int, metavar='', help='total number of steps in the averaging' )
parser.add_argument('-F', '--file', type=argparse.FileType('r'), nargs='+',
                    help='list of files the averaging, can be writen with space or with star')
args = parser.parse_args()
#file = "OSZICAR.2"
#firstStep = 10
#numStep = 500
new_firstStep = args.fir_step
new_numStep = args.num_steps
#print(new_firstStep, new_numStep)
#filelist1 = args.file
#print(filelist1)
#if args.file == None :
#    OSZICAR_main = "OSZICAR.1"
#else :
with open('OSZICAR_main', 'w') as outfile :
    for fname in args.file :
        print('reading ', fname)
        for line in fname :
            outfile.write(line)



#file_test = input("Enter OSZICAR filename/names separated with space: ")
#try :
#    a = re.findall('(.+)-n',file_test)[0]
#    file_list = a.split()
#except :
#    try :
#        a = re.findall('(.+)-f',file_test)[0]
#        file_list = a.split()
#    except :
#        a = file_test
#        file_list = a.split()
#print(a)
#file_list = a.split()
#print('reading',file_list)


#with open('OSZICAR_main', 'w') as outfile : # with open - you don't have to close
#    for fname in file_list :
#        with open(fname) as infile :
#            for line in infile:
#                outfile.write(line)


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
if new_numStep == None :
    numStep = count
    print('using the default number of steps, all: ',numStep)
else :
    numStep = new_numStep
    print(numStep, 'averaging steps were used')
#try :
    #numStep = int(re.findall('-n\s([0-9]+)',file_test)[0])
#    numStep = new_numStep
#except :
#    numStep = count
#    print('using the default number of steps, all: ',numStep)

if new_firstStep == None or new_firstStep >= numStep or new_firstStep < 0 :
    print('I will start from 0 step')
    firstStep = 0
else :
    firstStep = new_firstStep
    print('starting from ',firstStep,' interation')
#try :
    #firstStep = int(re.findall('-f\s([0-9]+)',file_test)[0])
    #firstStep = new_firstStep
#except :
    #firstStep = 0
#    print('starting from ',firstStep,' interation')

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
