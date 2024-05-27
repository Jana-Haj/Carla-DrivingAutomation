#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 09:08:26 2024

@author: Mariam
"""

import csv

import time

 

 

f=open("ex7.txt")

 

titles = ['Time', 'Acceleration', 'Speed', 'Throttle', 'Steer', 'Brake', 'Manual Throttle', 'Manual Brake','Heading','Location', 'Height','Rotation','Autopilot state','Light State','Time of intersection','notes']

data=[]

i=0
wait="none"

additionalInfo = "none"

 

file=open('ex7.csv', 'w')

writer = csv.writer(file)

writer.writerow(titles)

 
for line in f:

  
   if line.find(":")!=-1:
       
      line=line.split(": ")

      if line[0][:7]=="Time of":
         wait=line[1]
         continue
         
      if (line[0]=="Time" and i!=0):

         if wait!="none" and additionalInfo!="none":

            data.append(time.ctime(float(wait)))

            data.append(additionalInfo)

            wait="none"

            additionalInfo="none"

         elif wait!="none" and additionalInfo=="none":

            data.append(time.ctime(float(wait)))

            wait="none"

         elif wait =="none" and additionalInfo!="none":

            data.append(additionalInfo)

            additionalInfo="none"

         else:
            print("")#,end = "")

         writer.writerow(data)
         data=[]
         
   
      try: 

         dataString=float(line[1].strip())

      except:

         dataString=line[1].strip()
         
         
      if line[0]=="timeAutoOff" or line[0]=="timeAutoOn":

            dataString=line[0][8:]

            dataString+=" "

            dataString+= time.ctime(float(line[1].strip()))

 
      if line[0]=="Time":

         data.append(time.ctime(dataString))
         i+=1

      else:

         data.append(dataString)


 

   else:
       if (line[:7]=="control"):
           dataString=float(line[7:].strip())
           data.append(dataString)
           
       else:
           additionalInfo = line

 

file.close()