#!/usr/bin/bash
#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import math
import time
import sys
import os

x = np.linspace(-155.0, 155.0, 1000)
y = np.linspace(-155.0, 155.0, 1000)
  
X, Y = np.meshgrid(x,y)
 
F = ((X-2.49973)/149.595)**2 + ((Y-0.0)/149.574)**2 - 1.0
  
fig, ax = plt.subplots()
ax.contour(X,Y,F,[0],colors='b')
ax.set_aspect(1)
  
plt.xlim(-155.0, 155.0)
plt.ylim(-155.0, 155.0)
plt.xticks(np.arange(-155.0, 155.0 + 1.0, 31.0),rotation=45)
plt.yticks(np.arange(-155.0, 155.0 + 1.0, 31.0))
plt.grid(linestyle='--')

fig.set_dpi(100)
fig.set_size_inches(12.5, 7)

patch = [0, 1, 2, 3]
patch[0] = plt.Circle((-5, 5), 4.0, fc='c')
patch[1] = plt.Circle((-5, 5), 14.5, fc='y')
patch[2] = plt.Circle((-5, 5), 1.5, fc='b')
patch[3] = plt.Circle((-5, 5), 1.5, fc='b')

def init():
    patch[0].center = (152.1, 0)
    patch[1].center = (0, 0)
    patch[2].center = (5.0, 0)
    patch[3].center = (0.0, 0)
    ax.add_patch(patch[0])
    ax.add_patch(patch[1])
    ax.add_patch(patch[2])
    ax.add_patch(patch[3])
    ax.set_xlabel("Distance * 1E-09 meters")
    ax.set_ylabel("Distance * 1E-09 meters")

    fig.suptitle("View of the Earth's Elliptical Orbit (e=0.0167) from the Ecliptic North Pole", fontsize=14)

    ax.annotate('focus 2, 5E09 m left of the origin', xy=(7.5, 2.5), xytext=(36, 31), color='b',
    arrowprops=dict(ec='b',
    width=0.7, headwidth=4, headlength=4, shrink=0.05))

    ax.annotate('focus 1, center of the sun, i.e. coordinate system origin', xy=(0.0, 2.5), xytext=(0, 42.5), color='b',
    arrowprops=dict(ec='b',
    width=0.7, headwidth=4, headlength=4, shrink=0.05))

    bbox_props = dict(boxstyle="round", fc=(1.0, 1.0, 1.0), ec="g", lw=1)
    t = ax.text(283, 155.0, "The Sun should be 30X larger than shown for the size ratio of", ha="center", va="center", rotation=0,
        size=8,color='g', bbox=bbox_props)
    bb = t.get_bbox_patch()
    bb.set_boxstyle("round", pad=0.6)

    bbox_props = dict(boxstyle="round", fc=(1.0, 1.0, 1.0), ec="g", lw=1)
    t = ax.text(229.0, 124.0, "the Sun and Earth to be correct", ha="center", va="center", rotation=0,
        size=8,color='g', bbox=bbox_props)
    bb = t.get_bbox_patch()
    bb.set_boxstyle("round", pad=0.6)

    bbox_props = dict(boxstyle="round", fc=(1.0, 1.0, 1.0), ec="g", lw=1)
    t = ax.text(284, 93.0, "Considering the dimensions of the coordinate system, the Sun", ha="center", va="center", rotation=0,
        size=8,color='g', bbox=bbox_props)
    bb = t.get_bbox_patch()
    bb.set_boxstyle("round", pad=0.6)

    bbox_props = dict(boxstyle="round", fc=(1.0, 1.0, 1.0), ec="g", lw=1)
    t = ax.text(274, 62.0, "and the Earth are shown 2.0E05 and 6.2E05 times larger", ha="center", va="center", rotation=0,
        size=8,color='g', bbox=bbox_props)
    bb = t.get_bbox_patch()
    bb.set_boxstyle("round", pad=0.6)

    bbox_props = dict(boxstyle="round", fc=(1.0, 1.0, 1.0), ec="g", lw=1)
    t = ax.text(312, 31.0, "than their actual sizes, respectively", ha="center", va="center", rotation=0,
        size=8,color='g', bbox=bbox_props)
    bb = t.get_bbox_patch()
    bb.set_boxstyle("round", pad=0.6)

    return patch,

def animate(i):
    
##  the negative eccentricity is troubling (?)
##  note the pos x axis is pointing to the helicentric longitude of 282.9 deg, THEREFORE THE VERNAL EQUINOX IS AT 77.1 DEG)

    if i == 1:
        bbox_props = dict(boxstyle="rarrow", fc=(1.0, 1.0, 1.0), ec="b", lw=1)
        t = ax.text(138.0, 0.0, "A", ha="center", va="center", rotation=0,
            size=8, bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("rarrow", pad=0.6)
        bbox_props = dict(boxstyle="round", fc=(1.0, 1.0, 1.0), ec="b", lw=1)
        t = ax.text(-333.0, -124.0, "A = Aphelion at Ecliptic Lon=282.9 & Lat=0.0", ha="center", va="center", rotation=0,
            size=8, bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)
        bbox_props = dict(boxstyle="round", fc=(1.0, 1.0, 1.0), ec="b", lw=1)
        t = ax.text(-314.0, -155.0, "A = Earth at Minimum Velocity of 29,290 m/s, r = 152.1", ha="center", va="center", rotation=0,
            size=8, bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)

    if i == 77: # really 77.1
        bbox_props = dict(boxstyle="round", fc=(1.0, 1.0, 1.0), ec="r", lw=1)
        t = ax.text(-288, -93, "B = Vernal Equinox, Mar 19/20, Sun position at Ecliptic Lon=0 & Lat=0", ha="center", va="center", rotation=0,
            size=8,bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)
        bbox_props = dict(boxstyle="rarrow", fc=(1.0, 1.0, 1.0), ec="r", lw=1)
        t = ax.text(30.4, 132.6, "B", ha="center", va="center", rotation=77,
            size=8,bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("rarrow", pad=0.6)

    if i == 87: # really 86.3
        bbox_props = dict(boxstyle="round", fc=(1.0, 1.0, 1.0), ec="r", lw=1)
        t = ax.text(222, -31, "Ryker born on June 15, 2018", ha="center", va="center", rotation=0,
            size=8,bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)
        bbox_props = dict(boxstyle="round", fc=(1.0, 1.0, 1.0), ec="r", lw=1)
        t = ax.text(271, -62.0, "Sun Lon=266.3 & Lat=0.0, Earth at Lon 86.3 & Lat=0.0", ha="center", va="center", rotation=0,
            size=8, bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)
        bbox_props = dict(boxstyle="larrow", fc=(1.0, 1.0, 1.0), ec="r", lw=1)
        t = ax.text(8.8, 169.8, "Ryker", ha="center", va="center", rotation=87,
            size=8,bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("larrow", pad=0.6)

    if i == 87:
        
        bbox_props = dict(boxstyle="round", ec="b", fc="lightyellow", lw=1)
        t = ax.text(0.0, -93.0, "Year 2016, Ryker is -2 years old!", ha="center", va="center", rotation=0,
            size=10, color="r", bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)

    elif i == 447:
            
        bbox_props = dict(boxstyle="round", ec="b", fc="lightyellow", lw=1)
        t = ax.text(0.0, -93.0, "Year 2017, Ryker is -1 years old!", ha="center", va="center", rotation=0,
            size=10, color="r", bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)

    elif i == 807:
        
        bbox_props = dict(boxstyle="round", ec="b", fc="lightyellow", lw=1)
        t = ax.text(0.0, -93.0, "Year 2018,  Ryker is 0 years old!", ha="center", va="center", rotation=0,
            size=10, color="r", bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)

    elif i == 1167:
        
        bbox_props = dict(boxstyle="round", ec="b", fc="lightyellow", lw=1)
        t = ax.text(0.0, -93.0, "Year 2019,   Ryker is 1 year old!", ha="center", va="center", rotation=0,
            size=10, color="r", bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)

    elif i == 1527:

        bbox_props = dict(boxstyle="round", ec="b", fc="lightyellow", lw=1)
        t = ax.text(0.0, -93.0, "Year 2020,  Ryker is 2 years old!", ha="center", va="center", rotation=0,
            size=10, color="r", bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)

    elif i == 1887:

        bbox_props = dict(boxstyle="round", ec="b", fc="lightyellow", lw=1)
        t = ax.text(0.0, -93.0, "Year 2021,  Ryker is 3 years old!", ha="center", va="center", rotation=0,
            size=10, color="r", bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)

    elif i == 2247:

        bbox_props = dict(boxstyle="round", ec="b", fc="lightyellow", lw=1)
        t = ax.text(0.0, -93.0, "Year 2022,  Ryker is 4 years old!", ha="center", va="center", rotation=0,
            size=10, color="r", bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)

##    elif i == 2607:
##
##        bbox_props = dict(boxstyle="round", ec="b", fc="lightyellow", lw=1)
##        t = ax.text(0.0, -93.0, "Year 2023,  Ryker is 5 years old!", ha="center", va="center", rotation=0,
##            size=10, color="r", bbox=bbox_props)
##        bb = t.get_bbox_patch()
##        bb.set_boxstyle("round", pad=0.6)
##
##    elif i == 2967:
##
##        bbox_props = dict(boxstyle="round", ec="b", fc="lightyellow", lw=1)
##        t = ax.text(0.0, -93.0, "Year 2024,  Ryker is 6 years old!", ha="center", va="center", rotation=0,
##            size=10, color="r", bbox=bbox_props)
##        bb = t.get_bbox_patch()
##        bb.set_boxstyle("round", pad=0.6)
##
##    elif i == 3327:
##
##        bbox_props = dict(boxstyle="round", ec="b", fc="lightyellow", lw=1)
##        t = ax.text(0.0, -93.0, "Year 2025,  Ryker is 7 years old!", ha="center", va="center", rotation=0,
##            size=10, color="r", bbox=bbox_props)
##        bb = t.get_bbox_patch()
##        bb.set_boxstyle("round", pad=0.6)
##
##    elif i == 3687:
##
##        bbox_props = dict(boxstyle="round", ec="b", fc="lightyellow", lw=1)
##        t = ax.text(0.0, -93.0, "Year 2026,  Ryker is 8 years old!", ha="center", va="center", rotation=0,
##            size=10, color="r", bbox=bbox_props)
##        bb = t.get_bbox_patch()
##        bb.set_boxstyle("round", pad=0.6)
        
    else:

        bbox_props = dict(boxstyle="round", ec="b", fc= "lightyellow", lw=1)
        t = ax.text(0.0, 93.0, "", ha="center", va="center", rotation=0,
            size=8, color="r", bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)

    if i == 91:
        bbox_props = dict(boxstyle="round", fc=(1.0, 1.0, 1.0), ec="b", lw=1)
        t = ax.text(-301.0, -62.0, "C = Vertical (+) from Sun Focus at Ecliptic Lon=12.9 & Lat=0.0", ha="center", va="center", rotation=0,
            size=8, bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)
        bbox_props = dict(boxstyle="larrow", fc=(1.0, 1.0, 1.0), ec="b", lw=1)
        t = ax.text(0.0, 136.0, "C", ha="center", va="center", rotation=-90,
            size=8, bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("larrow", pad=0.6)

    if i == 100:  # really 99.1
        bbox_props = dict(boxstyle="round", fc=(1.0, 1.0, 1.0), ec="b", lw=1)
        t = ax.text(221, -93.0, "Enzo born on June 28, 2016", ha="center", va="center", rotation=0,
            size=8, bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)
        bbox_props = dict(boxstyle="round", fc=(1.0, 1.0, 1.0), ec="b", lw=1)
        t = ax.text(271, -124.0, "Sun Lon=279.1 & Lat=0.0, Earth at Lon 99.1 & Lat=0.0", ha="center", va="center", rotation=0,
            size=8, bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)
        bbox_props = dict(boxstyle="rarrow", fc=(1.0, 1.0, 1.0), ec="b", lw=1)
        t = ax.text(-26.4, 164.9, "Enzo", ha="center", va="center", rotation=-80.1,
            size=8, bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("rarrow", pad=0.6)

    if i == 100:

        bbox_props = dict(boxstyle="round", ec="b", fc="lightyellow", lw=1)
        t = ax.text(0.0, 93.0, "Year 2016,  Enzo is 0 years old!", ha="center", va="center", rotation=0,
            size=10, color="r", bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)
        
    elif i == 460:

        bbox_props = dict(boxstyle="round", ec="b", fc="lightyellow", lw=1)
        t = ax.text(0.0, 93.0, "Year 2017,   Enzo is 1 year old!", ha="center", va="center", rotation=0,
            size=10, color="r", bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)

        try:
            num = int(input('do you want to continue? enter 1 for yes and 0 for no, then press the return key:'))
        except ValueError:
            print("you did not enter a 0 or a 1, your entry will be ignored and the program will continue")
            num = 1
        if num == 1:
            print("you, or the program by default, entered a",num,", round we go for another revolution")
            print()
        elif num == 0:
            print("you entered a",num,", aborting the program, see you next time")
            print()
            time.sleep(2)
            sys.exit()
        else:
            print("no one should never see this output")
            
    elif i == 820:
        
        bbox_props = dict(boxstyle="round", ec="b", fc="lightyellow", lw=1)
        t = ax.text(0.0, 93.0, "Year 2018,  Enzo is 2 years old!", ha="center", va="center", rotation=0,
            size=10, color="r", bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)

        try:
            num = int(input('do you want to continue? enter 1 for yes and 0 for no, then press the return key:'))
        except ValueError:
            print("you did not enter a 0 or a 1, your entry will be ignored and the program will continue")
            num = 1
        if num == 1:
            print("you, or the program by default, entered a",num,", round we go for another revolution")
            print()
        elif num == 0:
            print("you entered a",num,", aborting the program, see you next time")
            print()
            sys.exit()
        else:
            print("no one should never see this output")

    elif i == 1180:
        
        bbox_props = dict(boxstyle="round", ec="b", fc="lightyellow", lw=1)
        t = ax.text(0.0, 93.0, "Year 2019,  Enzo is 3 years old!", ha="center", va="center", rotation=0,
            size=10, color="r", bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)

        try:
            num = int(input('do you want to continue? enter 1 for yes and 0 for no, then press the return key:'))
        except ValueError:
            print("you did not enter a 0 or a 1, your entry will be ignored and the program will continue")
            num = 1
        if num == 1:
            print("you, or the program by default, entered a",num,", round we go for another revolution")
            print()
        elif num == 0:
            print("you entered a",num,", aborting the program, see you next time")
            print()
            sys.exit()
        else:
            print("no one should never see this output")


    elif i == 1540:

        bbox_props = dict(boxstyle="round", ec="b", fc="lightyellow", lw=1)
        t = ax.text(0.0, 93.0, "Year 2020,  Enzo is 4 years old!", ha="center", va="center", rotation=0,
            size=10, color="r", bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)

        try:
            num = int(input('do you want to continue? enter 1 for yes and 0 for no, then press the return key:'))
        except ValueError:
            print("you did not enter a 0 or a 1, your entry will be ignored and the program will continue")
            num = 1
        if num == 1:
            print("you, or the program by default, entered a",num,", round we go for another revolution")
            print()
        elif num == 0:
            print("you entered a",num,", aborting the program, see you next time")
            print()
            sys.exit()
        else:
            print("no one should never see this output")

    elif i == 1900:

        bbox_props = dict(boxstyle="round", ec="b", fc="lightyellow", lw=1)
        t = ax.text(0.0, 93.0, "Year 2021,  Enzo is 5 years old!", ha="center", va="center", rotation=0,
            size=10, color="r", bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)

        try:
            num = int(input('do you want to continue? enter 1 for yes and 0 for no, then press the return key:'))
        except ValueError:
            print("you did not enter a 0 or a 1, your entry will be ignored and the program will continue")
            num = 1
        if num == 1:
            print("you, or the program by default, entered a",num,", round we go for another revolution")
            print()
        elif num == 0:
            print("you entered a",num,", aborting the program, see you next time")
            print()
            sys.exit()
        else:
            print("no one should never see this output")

    elif i == 2260:

        bbox_props = dict(boxstyle="round", ec="b", fc="lightyellow", lw=1)
        t = ax.text(0.0, 93.0, "Year 2022,  Enzo is 6 years old!", ha="center", va="center", rotation=0,
            size=10, color="r", bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)

        try:
            num = int(input('do you want to continue? enter 1 for yes and 0 for no, then press the return key:'))
        except ValueError:
            print("you did not enter a 0 or a 1, your entry will be ignored and the program will continue")
            num = 1
        if num == 1:
            print("you, or the program by default, entered a",num,", round we go for another revolution")
            print()
        elif num == 0:
            print("you entered a",num,", aborting the program, see you next time")
            print()
            sys.exit()
        else:
            print("no one should never see this output")

##    elif i == 2620:
##
##        bbox_props = dict(boxstyle="round", ec="b", fc="lightyellow", lw=1)
##        t = ax.text(0.0, 93.0, "Year 2023,  Enzo is 7 years old!", ha="center", va="center", rotation=0,
##            size=10, color="r", bbox=bbox_props)
##        bb = t.get_bbox_patch()
##        bb.set_boxstyle("round", pad=0.6)
##
##    elif i == 2980:
##
##        bbox_props = dict(boxstyle="round", ec="b", fc="lightyellow", lw=1)
##        t = ax.text(0.0, 93.0, "Year 2024,  Enzo is 8 years old!", ha="center", va="center", rotation=0,
##            size=10, color="r", bbox=bbox_props)
##        bb = t.get_bbox_patch()
##        bb.set_boxstyle("round", pad=0.6)
##
##    elif i == 3340:
##
##        bbox_props = dict(boxstyle="round", ec="b", fc="lightyellow", lw=1)
##        t = ax.text(0.0, 93.0, "Year 2025,  Enzo is 9 years old!", ha="center", va="center", rotation=0,
##            size=10, color="r", bbox=bbox_props)
##        bb = t.get_bbox_patch()
##        bb.set_boxstyle("round", pad=0.6)
##
##    elif i == 3700:
##
##        bbox_props = dict(boxstyle="round", ec="b", fc="lightyellow", lw=1)
##        t = ax.text(0.0, 93.0, "Year 2026, Enzo is 10 years old!", ha="center", va="center", rotation=0,
##            size=10, color="r", bbox=bbox_props)
##        bb = t.get_bbox_patch()
##        bb.set_boxstyle("round", pad=0.6)
        
    else:

        bbox_props = dict(boxstyle="round", ec="b", fc= "lightyellow", lw=1)
        t = ax.text(0.0, 93.0, "", ha="center", va="center", rotation=0,
            size=8, color="r", bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)

    if i == 167: # really 167.1
        bbox_props = dict(boxstyle="round", fc=(1.0, 1.0, 1.0), ec="r", lw=1)
        t = ax.text(-295.0, -31.0, "D = Summer Solestice, Jun 20/21, Sun Position at Lon=90 & Lat=0", ha="center", va="center", rotation=0,
            size=8, bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)
        bbox_props = dict(boxstyle="larrow", fc=(1.0, 1.0, 1.0), ec="r", lw=1)
        t = ax.text(-129.6, 29.7, "D", ha="center", va="center", rotation=-12.9,
            size=8, bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("larrow", pad=0.6)
    if i == 181:
        bbox_props = dict(boxstyle="round", fc=(1.0, 1.0, 1.0), ec="b", lw=1)
        t = ax.text(-330.0, 62.0, "E = Perihelion at Ecliptic Lon=102.9 & Lat=0.0", ha="center", va="center", rotation=0,
            size=8, bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)
        bbox_props = dict(boxstyle="round", fc=(1.0, 1.0, 1.0), ec="b", lw=1)
        t = ax.text(-313.0, 31.0, "E = Earth at Maximum Velocity of 30,290 m/s, r = 147.1", ha="center", va="center", rotation=0,
            size=8, bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)
        bbox_props = dict(boxstyle="larrow", fc=(1.0, 1.0, 1.0), ec="b", lw=1)
        t = ax.text(-134.0, 0.0, "E", ha="center", va="center", rotation=0,
            size=8, bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("larrow", pad=0.6)
    if i == 257: # really 257.1
        bbox_props = dict(boxstyle="round", fc=(1.0, 1.0, 1.0), ec="r", lw=1)
        t = ax.text(-291.0, 93.0, "F = Autumnal Equinox, Sep 22/23, Sun Position at Lon=180 & Lat=0", ha="center", va="center", rotation=0,
            size=8, bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)
        bbox_props = dict(boxstyle="larrow", fc=(1.0, 1.0, 1.0), ec="r", lw=1)
        t = ax.text(-30.3, -132.6, "F", ha="center", va="center", rotation=77.1,
            size=8, bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("larrow", pad=0.6)
    if i == 271:
        bbox_props = dict(boxstyle="round", fc=(1.0, 1.0, 1.0), ec="b", lw=1)
        t = ax.text(-299.0, 124.0, "G = Vertical (-) from Sun Focus at Ecliptic Lon=192.9 & Lat=0.0", ha="center", va="center", rotation=0,
            size=8, bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)
        bbox_props = dict(boxstyle="rarrow", fc=(1.0, 1.0, 1.0), ec="b", lw=1)
        t = ax.text(0.0, -136.0, "G", ha="center", va="center", rotation=-90,
            size=8, bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("rarrow", pad=0.6)
    if i == 347: # really 347.1
        bbox_props = dict(boxstyle="round", fc=(1.0, 1.0, 1.0), ec="r", lw=1)
        t = ax.text(-294.0, 155.0, "H = Winter Solestice, Dec 21/22, Sun Position at Lon=270 & Lat=0", ha="center", va="center", rotation=0,
            size=8, bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("round", pad=0.6)
        bbox_props = dict(boxstyle="rarrow", fc=(1.0, 1.0, 1.0), ec="r", lw=1)
        t = ax.text(133.5, -30.6, "H", ha="center", va="center", rotation=-12.9,
            size=8, bbox=bbox_props)
        bb = t.get_bbox_patch()
        bb.set_boxstyle("rarrow", pad=0.6)
    r = 149.55323 / (1.0 - 0.01671 * np.cos(np.radians(i)))
    x = 0.0 + r * np.cos(np.radians(i))
    y = 0.0 + r * np.sin(np.radians(i))
    patch[0].center = (x, y)
    return patch,

anim = animation.FuncAnimation(fig, animate, 
                               init_func=init,  
                               frames=2520, 
                               interval=1,repeat=False,
                               blit=False)

print("plt.show")

##plt.figure() # not needed
##plt.get_current_fig_manager().full_screen_toggle() # toggle fullscreen mode... but i want maximized window that i can toggle

##mng = plt.get_current_fig_manager()
##mng.frame.Maximize(True)

##figManager = plt.get_current_fig_manager()
##figManager.window.showMaximized()

plt.show()

sys.exit()
