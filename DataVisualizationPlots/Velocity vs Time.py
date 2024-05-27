#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:09:33 2024

"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 15:20:24 2024

@author: justin
"""

import csv

import matplotlib.pyplot as plt

import numpy as np

 

def read_points_from_csv(filename, x_column,y_column):

    Xpoints = []
    Ypoints = []
    x=0
    xt=[]
    
    with open(filename, 'r') as file:

        csv_reader = csv.reader(file)

        for row in csv_reader:
            try:
                
            
    
                Ypoints.append(float(row[y_column]))
                loc= row[9]

               
                floats= loc.strip("()").split(",")
                SF1=False
                SF2=False
                if (abs(float(floats[0])+88)<10 and abs(float(floats[1])-124)<10 and SF1==False) or  (abs(float(floats[0])+11)<20 and abs(float(floats[1])-134)<20 and  SF2==False)  :
                    if x==0:
                        xt.append("here")
                        x=1
                        if SF1 == False:
                            SF1=True
                        else:
                            SF2 = True
                    else:
                        xt.append("")
                    
                else:
                    x=0
                    xt.append("")
                        
                    
                   
                    #floats= strr.strip("()").split(",")
                
    
     
    
                   
    
    #                points.append((float(floats[0]), float(floats[1])))
    
            except(IndexError, ValueError):
                   
                    pass  # Skip rows that don't have valid data or format errors
    print(len(Ypoints))
    print(len(xt))
    Xpoints= [x for x in range (len(Ypoints))]
    
    return [Xpoints,Ypoints,xt]

 

def plot_points(points):

#    x_values = [point[0] for point in points]
#
#    y_values = [point[1] for point in points]
    
    x_values=points[0]
    y_values=points[1]
#    color= np.random.rand(len(points))

# =============================================================================
#    plt.scatter(x_values[1],y_values[1], c= 'red', marker ='X')
# =============================================================================

    plt.plot(x_values, y_values, c='blue' ,marker='.', label='Velocity')
    for i in range (len(points[2])):
        if points[2][i]=="here":
            plt.scatter(i,0,c='red', marker='X',label ='Silent Failure')
    
    plt.title('Velocity vs Time')

    plt.xlabel('Time')

    plt.ylabel('Velocity')

    plt.grid(True)
    handles, labels = plt.gca().get_legend_handles_labels()
    plt.legend(handles[:2], labels[:2])
    plt.show()

 

# Example usage:

if __name__ == "__main__":

    filename = 'ex5.csv'  # Name of your CSV file

    x_column = 9  # Index of the column containing X values (zero-based indexing)

    y_column = 2  # Index of the column containing Y-value VELOCITY  (zero-based indexing)

   

    points = read_points_from_csv(filename, x_column, y_column)

  

    

    plot_points(points)

