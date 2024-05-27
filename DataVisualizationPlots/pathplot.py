#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 15:20:24 2024

"""

import csv

import matplotlib.pyplot as plt

import numpy as np

 

def read_points_from_csv(filename, x_column):

    points = []
    auto = []

    with open(filename, 'r') as file:

        csv_reader = csv.reader(file)

        for row in csv_reader:

            try:

                strr= row[x_column]

               
                floats= strr.strip("()").split(",")

 

               

                points.append((float(floats[0]), float(floats[1])))
                
                if row[12][0:3]=="Off":
                    auto.append('blue')
                else:
                    auto.append('green')

            except (IndexError, ValueError):

                pass  # Skip rows that don't have valid data or format errors

    return [points,auto]

 

def plot_points(points):

    x_values = [-point[0] for point in points[0]]

    y_values = [point[1] for point in points[0]]

    color= np.random.rand(len(points))

    # color
   
    # plt.scatter(x_values, y_values,c = 'green'  ,marker='.')
    plt.scatter(x_values, y_values,c = points[1] ,marker='.')
    plt.scatter(x_values[0],y_values[0], c= 'black', marker ='X', label='Starting point')
    x1=[-103,-88.1,171.2,102.5,-148.9,-103,-25.4]
    y=[0.5,125.7,-207.6,-205.5,-15.7,135.9,134.6]
    #plt.scatter(86, 177, c= 'blue', marker ='X')
   
    x = [-x for x in x1]
    plt.scatter(x,y, c= 'red', marker ='X', label='red traffic lights' )

    plt.title('Path')    

    plt.xlabel('X')

    plt.ylabel('Y')
    plt.scatter(108,0.3, -159, c= 'red', marker ='x')
    plt.xlim(-270,170)
    plt.ylim(-220,220)
    

    plt.grid(True)
    
    # plt.legend()
    plt.show()
 

# Example usage:

if __name__ == "__main__":

    filename = 'ex7.csv'  # Name of your CSV file

    x_column = 9  # Index of the column containing X values (zero-based indexing)

   # y_column = 1  # Index of the column containing Y values (zero-based indexing)

   

    points = read_points_from_csv(filename, x_column)

  

    

    plot_points(points)

