# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:05:02 2024

@author: User
"""

import csv
import matplotlib.pyplot as plt
import numpy as np

fil ='ex5'
fill = "ex5"

def read_points_from_csv(filename,yb_column,yt_column,ya_column,ymanualbrake,ymanualthrottle):

 

    Xpoints = []

    Ytpoints = []

    Ybpoints = []

    Yapoints = []
    
    Y_manualbrake = []
    Y_manualthrottle = []
    
    

    rangee=[]

    locations=[]

    with open(filename, 'r') as file:

        csv_reader = csv.reader(file)
        for row in csv_reader:
            try:

                Ytpoints.append(float(row[yt_column]))

                Ybpoints.append(float(row[yb_column]))
                
                Y_manualbrake.append(float(row[ymanualbrake]))
                
                Y_manualthrottle.append(float(row[ymanualthrottle]))
                
                

                locations.append(row[9])

                if row[ya_column][0:3] == "Off":

                    Yapoints.append(1)

                else:

                    Yapoints.append(0)

                #floats= strr.strip("()").split(",")
                #points.append((float(floats[0]), float(floats[1])))

            except (IndexError, ValueError):


                pass  # Skip rows that don't have valid data or format errors


    x=[]
    sf1=False
    sf2=False
  
    

    for i in range (len(Yapoints)):
        
        strr= locations[i]
        
        floats= strr.strip("()").split(",")
        print(floats)
        
        if (sf1 == False)  and (abs(float(floats[0])+88)<10 and abs(float(floats[1])-124)<10) :
                x.append(i)
                sf1=True
        
        
        if (sf2 == False) and (abs(float(floats[0])+11)<15 and abs(float(floats[1])-134)<15)  :
            x.append(i)
            sf2=True

        if sf1==True and sf2==True:
            break

    Xpoints= [x for x in range (len(Yapoints))]
    rangee= [ x[0]-20, x[0]+50, x[1]-20, x[1]+50 ]

    return [Xpoints,Ytpoints,Ybpoints,Yapoints,Y_manualbrake,rangee,Y_manualthrottle]
 

 

def plot_points(points):
    x_values=points[0]
    yt_values =points[1]
    yb_values = points[2]
    ya_values = points[3]
   # ya_values= [abs(1-x) for x in ya_values ]
    rangee=points[4]
    brakemanual = points[4]
    throttlemanual = points[6]
    autobrake = [x - y for x, y in zip(yb_values, brakemanual)]
    
#    color= np.random.rand(len(points))

    # plt.scatter(x_values[1],y_values[1], c= 'red', marker ='X')
    # plt.figure(1)
    # plt.plot(x_values[rangee[0]:rangee[1]], ya_values[rangee[0]:rangee[1]] , c = 'red' ,marker='.', label = 'auto' )
    # plt.plot(x_values[rangee[0]:rangee[1]], yb_values[rangee[0]:rangee[1]] , c = 'blue' ,marker='.', label = 'brake')
    # plt.scatter(x_values[rangee[0]:rangee[1]], yt_values[rangee[0]:rangee[1]] , c = 'black' ,marker='.', label = 'throttle' )
    # plt.plot(x_values[rangee[0]:rangee[1]], brakemanual[rangee[0]:rangee[1]] , c = 'purple' ,marker='.', label = 'manual  brake' )
    # # plt.plot(x_values[rangee[0]:rangee[1]], throttlemanual[rangee[0]:rangee[1]] , c = 'green' ,marker='.', label = 'manual  throttle' )
    # # plt.plot(x_values[rangee[0]:rangee[1]], autobrake[rangee[0]:rangee[1]] , c = 'pink' ,marker='.', label = 'auto brake' )
    # plt.title('SF1 (auto,throttle,brake)')
    # plt.xlabel('time')
    # # plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    
    
    # plt.figure(2)
    # plt.plot(x_values[rangee[2]:rangee[3]], ya_values[rangee[2]:rangee[3]] , c = 'red' ,marker='.', label = 'auto')
    # plt.plot(x_values[rangee[2]:rangee[3]], yb_values[rangee[2]:rangee[3]] , c = 'blue' ,marker='.', label = 'brake')
    # plt.scatter(x_values[rangee[2]:rangee[3]], yt_values[rangee[2]:rangee[3]] , c = 'black' ,marker='.', label = 'throttle' )
    # plt.plot(x_values[rangee[2]:rangee[3]], brakemanual[rangee[2]:rangee[3]] , c = 'purple' ,marker='.', label = 'manual  brake' )
    # plt.plot(x_values[rangee[2]:rangee[3]], throttlemanual[rangee[2]:rangee[3]] , c = 'green' ,marker='.', label = 'manual  throttle' )
    # # plt.plot(x_values[rangee[2]:rangee[3]], autobrake[rangee[2]:rangee[3]] , c = 'pink' ,marker='.', label = 'auto brake' )

    # plt.title('SF2 (auto,throttle,brake)')
    # plt.xlabel('time')
    # # plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    
    # plt.figure(3)
    # plt.plot(x_values, ya_values , c = 'red' ,marker='.' ,label = 'auto')
    # plt.plot(x_values, yb_values , c = 'blue' ,marker='.', label = 'brake')
    # plt.scatter(x_values, yt_values , c = 'black' ,marker='.', label = 'throttle' )
    # plt.plot(x_values, brakemanual , c = 'purple' ,marker='.', label = 'manual  brake' )
    # plt.plot(x_values, throttlemanual , c = 'green' ,marker='.', label = 'manual  throttle' )
    # # plt.plot(x_values, autobrake , c = 'pink' ,marker='.', label = 'auto brake' )
    plt.figure(3)
    plt.plot(x_values[45:75], ya_values[45:75] , c = 'red' ,marker='.' ,label = 'auto')
    plt.plot(x_values[45:75], yb_values[45:75] , c = 'blue' ,marker='.', label = 'brake')
    plt.scatter(x_values[45:75], yt_values[45:75] , c = 'black' ,marker='.', label = 'throttle' )
    plt.plot(x_values[45:75], brakemanual[45:75] , c = 'purple' ,marker='.', label = 'manualbrake' )
    plt.plot(x_values[45:75], throttlemanual[45:75] , c = 'green' ,marker='.', label = 'manualthrottle' )
    
    # plt.figure(3)
    # plt.plot(x_values[325:], ya_values[325:] , c = 'red' ,marker='.' ,label = 'auto')
    # plt.plot(x_values[325:], yb_values[325:] , c = 'blue' ,marker='.', label = 'brake')
    # plt.scatter(x_values[325:], yt_values[325:] , c = 'black' ,marker='.', label = 'throttle' )
    # plt.plot(x_values[325:], brakemanual[325:] , c = 'purple' ,marker='.', label = 'manual  brake' )
    # plt.plot(x_values[325:], throttlemanual[325:] , c = 'green' ,marker='.', label = 'manual  throttle' )
    # plt.plot(x_values, autobrake , c = 'pink' ,marker='.', label = 'auto brake' )

    plt.xlabel('time')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    
    # plt.ylabel('Y')

    plt.grid(True)

    plt.show()
 



 

# Example usage:

 

if __name__ == "__main__":

 

    filename = fil + '.csv'  # Name of your CSV file

 

    x_column = 2  # Index of the column containing X values (zero-based indexing)

 

    yb_column = 5  # Index of the column containing Y values (zero-based indexing)

    yt_column = 3

    ya_column = 12
    
    ymanualbrake= 7
    ymanualthrottle = 6
    

 
    points = read_points_from_csv(filename, yb_column,yt_column,ya_column,ymanualbrake,ymanualthrottle)

 
    plot_points(points)

 