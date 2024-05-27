# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 00:28:48 2024

@author: User
"""
fil = 'ex4'
fill = "ex"
import csv
import math 
import matplotlib.pyplot as plt

import numpy as np

def read_points_from_csv(filename):

    points = []
    x=0
    SF1=False
    SF2=False
    with open(filename, 'r') as file:

        csv_reader = csv.reader(file)

        for row in csv_reader:
            try:
               
                loc= row[9]
                floats= loc.strip("()").split(",")
                if row[12][0:2]!="On":
                    if x==0:
                        if (SF1== False) and (abs(float(floats[0])+88)<20 and abs(float(floats[1])-124)<20):
                            SF1 = True
                            x=1
                            points.append(math.sqrt(((float(floats[0])+87.936958)**2) + ((float(floats[1])-127.373306)**2)))
                        if (SF2== False) and (abs(float(floats[0])+11)<20 and abs(float(floats[1])-134)<20):
                            x=1
                            SF2 =True
                            
                            points.append(math.sqrt(((float(floats[0])+11.351341)**2) + ((float(floats[1])-134.227509)**2)))
                else: 
                    x=0
            except (IndexError, ValueError):
                
                pass  # Skip rows that don't have valid data or format errors
            
    return points

def plot_points(points):
    plt.bar(["SF1","SF2"],points)
    for i, value in enumerate(points):
        plt.text(i, value, str(value), ha='center')
    plt.xlabel('Silent Failure')
    plt.ylabel('Distance to Intersection (m)')
    plt.title('Distance to Intersection (m)')

if __name__ == "__main__":

    filename = fil +'.csv'  # Name of your CSV file
    points = read_points_from_csv(filename)
    plot_points(points)